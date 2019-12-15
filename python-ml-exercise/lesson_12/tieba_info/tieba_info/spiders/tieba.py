# -*- coding: utf-8 -*-
import scrapy
from urllib.request import urljoin

class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E6%96%87%E5%AD%A6%E5%90%A7&fr=search']

    def parse(self, response):
        print('-----------')
        url_list = response.css('.j_th_tit::attr(href)').extract()

        #遍历帖子的url地址，解析每个帖子的具体内容
        for url in url_list:
            yield scrapy.Request(url=urljoin(response.url, url), callback=self.page_analyes1)
        #获取下一页的url地址继续交由爬虫处理
        next = response.css(".next.pagination-item::attr('href')").extract()
        if next:
            yield scrapy.Request(url=urljoin(response.url, next), callback=self.parse)

    #解析帖子内容
    def page_analyes1(self, response):
        #texts = response.css('.d_post_content.j_d_post_content::text').getall()
        print('当前爬取的地址是：{}'.format(response.url))
        #获取当前标题
        tit = response.css('.core_title_txt.pull-left.text-overflow::text').get()
        if tit:
            #获取帖子内容
            text_list = response.css('.d_post_content.j_d_post_content::text').getall()
            #获取作者名字
            author = response.xpath('//li[@class="d_name"]/a/text()').extract()
            #获取几楼和时间
            floor_list, sendtime_list = self.get_time_floor(response)
            for i in range(len(author)):
                print(text_list[i])
                print(author[i])
                print(floor_list[i])
                print(sendtime_list[i])
            next_page = response.css('.l_pager.pager_theme_5.pb_list_pager a::attr(herf)').extract()
            if next_page:
                scrapy.Request(url=urljoin(response.url, next_page[-2]), callback=self.page_analyes1())

    def get_time_floor(self, response):
        all_bottom = response.css('.tail-info::text').getall()
        floorandtime = [info for info in all_bottom if info != '来自']
        floor = [floorandtime[i] for i in range(len(floorandtime)) if i % 2 == 0]
        print('-----111---------')
        print(floor)
        print('-----111---------')
        time = [floorandtime[i] for i in range(len(floorandtime)) if i % 2 == 1]
        print('-----111---------')
        print(time)
        print('-----111---------')
        for i in range(len(floor)):
            print(floor[i])
            print(time[i])
        return floor, time

