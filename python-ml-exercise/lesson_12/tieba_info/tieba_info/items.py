# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    reply_time = scrapy.Field()
    floor = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into my_tieba_info(title, author, content, reply_time, floor)
            values (%s, %s, %s, %s, %s)
        
        """
        params = (self['title'], self['author'], self['content'], self['reply_time'], self['floor'])
        return insert_sql, params

