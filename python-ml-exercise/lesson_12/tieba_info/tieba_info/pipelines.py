# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql as mdb
import pymysql
import pymysql.cursors

class TiebaInfoPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_NAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASS'],
            charset='utf8',
            use_unicode=True,
        )
        dbpool = pymysql.connect(**dbparams)
        return dbpool

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.do_insert, item)

    def do_insert(self, conn, item):
        insert_sql, params = item.get_insert_sql()
        conn.execute(insert_sql, params)
