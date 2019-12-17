# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql as mdb
import pymysql
import pymysql.cursors
#from scrapy import settings
from items import TiebaInfoItem

class TiebaInfoPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'admin',
            db = 'tieba',
            charset = 'utf8'
        )
        self.cursor = self.connect.cursor()

    # @classmethod
    # def from_settings(cls, settings):
    #     dbparams = dict(
    #         host=settings['MYSQL_HOST'],
    #         db=settings['MYSQL_NAME'],
    #         user=settings['MYSQL_USER'],
    #         passwd=settings['MYSQL_PASS'],
    #         charset='utf8',
    #         use_unicode=True,
    #     )
    #     dbpool = pymysql.connect(**dbparams)
    #     return cls(dbpool)

    def process_item(self, item, spider):
        insert_sql, params = item.get_insert_sql()
        self.cursor.execute(insert_sql, params)
        self.connect.commit()

    def close(self,spider):
        self.cursor.close()
        self.connect.close()

