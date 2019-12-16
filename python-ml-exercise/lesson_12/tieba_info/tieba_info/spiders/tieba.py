# -*- coding: utf-8 -*-
import scrapy
from urllib.request import urljoin
from tieba_info.items import TiebaInfoItem
import re

class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%CE%C4%D1%A7&fr=ala0&loc=rec']

    def parse(self, response):
        print('-----------')
        url_list = response.css('.j_th_tit::attr(href)').extract()

        #遍历帖子的url地址，解析每个帖子的具体内容
        for url in url_list:
            yield scrapy.Request(url=urljoin(response.url, url), callback=self.page_analyes1)
        #获取下一页的url地址继续交由爬虫处理
        next = response.css(".next.pagination-item::attr('href')").extract()[0]
        if next:
            yield scrapy.Request(url=urljoin(response.url, next), callback=self.parse)

    #解析帖子内容
    def page_analyes1(self, response):
        print('===========================================================')
        #texts = response.css('.d_post_content.j_d_post_content::text').getall()
        print('当前爬取的地址是：{}'.format(response.url))
        #获取当前标题
        tit = response.css('.core_title_txt.pull-left.text-overflow::text').get()
        print('当前帖子标题为：',tit)
        if tit:
            #获取帖子内容
            text_lists = response.css('.d_post_content.j_d_post_content').getall()
            text_list = []
            for text in text_lists:
                ret = re.compile(r"[\u4e00-\u9fa5]+").findall(text)
                text_list.append(ret)
            #获取作者名字
            authors_ = response.xpath('//li[@class="d_name"]/a').getall()
            authors = []
            for itm in authors_:
                about_author = re.findall('>.*?<', itm)
                every_author = [i.replace(' ', '').replace('>', '').replace('<', '') for i in about_author]
                authors.append(''.join(every_author))
            # print('当前帖子下的作者人数：'.format(len(author)))
            #获取几楼和时间
            floor_list, sendtime_list = self.get_time_floor(response)
            #print(floor_list)
            for i in range(len(floor_list)):
                tieba_item = TiebaInfoItem()
                tieba_item['title'] = tit
                tieba_item['author'] = authors[i]
                tieba_item['content'] = text_list[i]
                tieba_item['reply_time'] = sendtime_list[i]
                tieba_item['floor'] = floor_list[i]
                yield tieba_item
                # print('------内容-------')
                # print(text_list[i])
                # print('-----------------')
                # print(authors[i])
                # print(floor_list[i])
                # print(sendtime_list[i])
            next_page = response.css('.l_pager.pager_theme_5.pb_list_pager a::attr(herf)').extract()
            if next_page:
                scrapy.Request(url=urljoin(response.url, next_page[-2]), callback=self.page_analyes1())

    def get_time_floor(self, response):
        all_bottom = response.css('div span.tail-info::text').getall()
        floorandtime = [info for info in all_bottom if info != '来自']
        floor = [floorandtime[i] for i in range(len(floorandtime)) if i % 2 == 0]
        print(floor)
        time = [floorandtime[i] for i in range(len(floorandtime)) if i % 2 == 1]
        print(time)
        for i in range(len(floor)):
            print(floor[i])
            print(time[i])
        return floor, time

