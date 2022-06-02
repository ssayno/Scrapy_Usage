# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
import string

from itemadapter import ItemAdapter
import os


class LPipeline:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_spider(self, spider):
        if not os.path.exists("./Content"):
            os.mkdir("./Content")
        with open("Content/" + f"{self.file_name}.tex", "w") as f:
            f.write("\chapter{火之晨曦}")

    def process_item(self, item, spider):

        with open("Content/" + f"{self.file_name}.tex", "a+") as f:
            contents = self.replace_tex_orgin_symbol(item["content"])
            title = self.replace_tex_orgin_symbol(item["title"])
            if title != "" and title is not None:
                title = f"\n\section{{{title.split()[1].replace('(', r' --').replace(')', r'--')}}}"
                f.write(title + "\n" + contents)
            else:
                f.write(contents)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            file_name=crawler.settings.get("FILE_NAME")
        )

    def replace_tex_orgin_symbol(self, content):
        if content is None:
            return content
        contents = re.subn("(^\u3000{2})|(^\xa0+}{2})(^$)|(③≠八③≠八③≠读③≠书，.↗.o●)|(\bxdx\b)|(▲≥八▲≥八▲≥读▲≥书，.√.≧o)", "", content)[0]
        contents = re.subn("([$%^#~_&])+", r"\\\1", contents)[0]
        return contents
