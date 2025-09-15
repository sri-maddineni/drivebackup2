# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Pro1Pipeline(object):

    def __init__(self):
        self.createcon()
        self.createtable()


        pass

    def createcon(self):
        self.con=sqlite3.connect("dbase.db")
        self.cur=self.con.cursor()

    def createtable(self):
        self.cur.execute('''drop table if exists dataasetable ''')
        self.cur.execute(
            '''create table  dataasetable (
                                    title text,
                                    author text
                                    )
            '''
            )

    def storedb(self,item):
        self.cur.execute('''
        insert into dataasetable values(?,?)
        ''',
        (
         item['title'][0],
         item['author'][0]
         )
    )

        self.con.commit()

    def process_item(self, item, spider):
        self.storedb(item)
        print("title name abc: "+item["title"][0])

        return item


