#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-06 15:52:25
# Project: newv2ex

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.v2ex.com/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="https://www.v2ex.com/?tab="]').items():
            self.crawl(each.attr.href, callback=self.tab_page)
    @config(priority=2)
    def tab_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
