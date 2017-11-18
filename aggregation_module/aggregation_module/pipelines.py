# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient
import logging


class MongoWriterPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient(
            'mongodb://underpriced:mongounderpriced@45.55.210.115/underpriced?authMechanism=SCRAM-SHA-1')
        self.db = self.client.underpriced

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db['unprocessedFlats'].replace_one(
            {'_id': item['_id']},
            item,
            upsert=True)
        return item
