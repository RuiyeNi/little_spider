# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import MySQLdb
import os


class CarlingoPipeline(object):
    def __init__(self):
        self.setupDBcon()
        self.createTables()
        print '--------------__init__ -----------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'

    def setupDBcon(self):
        #self.con = MySQLdb.connect(os.getcwd() + 'scrapyDB.db')
        self.con = MySQLdb.connect(host = "localhost", user = "root", passwd = "12345")
        self.cur = self.con.cursor()
        self.cur.execute("DROP DATABASE IF EXISTS scrapyDB")
        self.cur.execute("CREATE DATABASE IF NOT EXISTS scrapyDB")
        self.cur.execute("USE scrapyDB")
        print '--------------setupDBcon -----------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'

    def createTables(self):
        self.dropCarlingoTable()
        self.createCarlingoTable()
        print '--------------createTables -----------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'

    def dropCarlingoTable(self):
        #drop carlingo table if exists
        self.cur.execute("DROP TABLE IF EXISTS carlingo")
        print '--------------dropCarlingoTable-------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'

    def closeDB(self):
        self.con.close()
        print '-------------closeDB------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'

    def __del__(self):
        self.closeDB()
        print '--------------__del__ -----------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'

    def createCarlingoTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS carlingo(id INT PRIMARY KEY AUTO_INCREMENT, \
            title VARCHAR(25), \
            price VARCHAR(25), \
            location VARCHAR(25) \
            )")
        print '-----------creatCarlingoTable---------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'

    def storeInDb(self, item):
        self.cur.execute("INSERT INTO carlingo(\
            title, \
            price, \
            location \
            ) \
        VALUES( ?, ?, ?)", \
        ( \
            item.get('title',''),
            item.get('price',''),
            item.get('location','')
        ))
        print '------------------------'
        print 'Data Stored in Database'
        print '------------------------'
        self.con.commit()

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print "--------get_media_requests-------"
            print '--------------------------------------'
            print '--------------------------------------'
            print '--------------------------------------'
            print '--------------------------------------'
            yield scrapy.Request(image_url)


    def item_completed(self, results, item, info):
        print "--------item_completed-------"
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        print '--------------------------------------'
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item