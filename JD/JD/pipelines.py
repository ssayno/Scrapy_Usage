# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JdPipeline:
    def __init__(self, host, name, password, db):
        self.cursor = None
        self.connection = None
        self.host = host
        self.name = name
        self.password = password
        self.db = db

    def open_spider(self, spider):
        pymysql.install_as_MySQLdb()
        self.connection = pymysql.connect(
            host=self.host,
            user=self.name,
            password=self.password,
            db=self.db,
            port=3306,
            charset="utf8mb4",
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        insert_sql = f'insert into phone value(\'{item["name"]}\',\'{item["price"]}\', \'{item["manufacturer"]}\')'
        try:
            self.cursor.execute(insert_sql)
            self.connection.commit()
        except Exception as e:
            print(insert_sql)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            name=crawler.settings.get('MYSQL_NAME'),
            password=crawler.settings.get("MYSQL_PASSWORD"),
            db=crawler.settings.get("MYSQL_DATABASE")
        )

    def close_spider(self, spider):
        if self.connection is not None:
            self.connection.close()
