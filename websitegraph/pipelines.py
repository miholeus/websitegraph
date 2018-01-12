# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class WebsitegraphPipeline(object):
    def process_item(self, item, spider):
        cur_url = item["current_url"]
        ref_url = item["referring_url"]
        if ref_url is not None:
            try:
                ref_url = ref_url.decode("utf-8")
            except AttributeError:
                pass

        return json.dumps({
            'depth': item["depth"],
            'current_url': cur_url,
            'referring_url': ref_url
        })
