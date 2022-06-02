# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class LongzuPipeline:
    def process_item(self, item, spider):
        if not os.path.exists("./Content"):
            os.mkdir("./Content")
        if item["title"] is None or item["title"] == "None":
            return item
        with open("Content/" + "Dragon.tex", "a+") as f:
            content = item["content"]
            content.replace("$", "\\$").replace("%", "\\%")
            if item["title"] != "":
                title = f"\n\section{{ {item['title'].split()[1].replace('(', '->').replace(')', '')} }}"
            else:
                title = ""
            f.write(title + "\n" + item["content"])
        return item

