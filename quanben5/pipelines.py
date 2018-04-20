# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = 'root',
            db = 'artproject',
            charset = 'utf8'
        )
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        cols,valuse = zip(*item.items())
        sql = 'insert into `%s` (%s) values (%s)' % \
              (item.table,
                ','.join(['`%s`' % k for k in cols]),
                ','.join(['%s']*len(cols)))

        # print(sql)
        try:
            self.cur.execute(sql,valuse)
        except Exception as e:
            print(e)

        self.conn.commit()
        print(self.cur._last_executed)
        return item