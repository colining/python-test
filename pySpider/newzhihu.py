#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-06 18:09:52
# Project: newzhihu

from pyspider.libs.base_handler import *
import re
import random
import MySQLdb


class Handler(BaseHandler):
    crawl_config = {
        'headers': {
            'User-Agent': 'GoogleBot',
            'Host': 'www.zhihu.com'
        }
    }

    def __init__(self):
        self.db = MySQLdb.connect('127.0.0.1', 'root', '86271325', 'wenda', charset='utf8')

    def add_question(self, title, content,comment_count):
        try:
            cursor = self.db.cursor()
            sql = 'insert into question(title, content, user_id, created_date, comment_count) values ("%s","%s",%d, %s, %d)' % (
            title, content, random.randint(1, 10), 'now()',comment_count);
            print sql
            cursor.execute(sql)
            qid =  cursor.lastrowid
            self.db.commit()
            return qid
        except Exception, e:
            print e
            self.db.rollback()
        return 0

    # 插入评论
    def add_comment(self, qid, comment):  # 根据问题的ID，然后插入对应的评论
        try:
            cursor = self.db.cursor()
            sql = 'insert into comment(content, user_id, entity_id, entity_type, created_date) values ("%s","%d",%d, %d, %s)' % (
                comment, random.randint(1, 10), 1, qid, 1, 'now()');
            # print sql
            cursor.execute(sql)
            self.db.commit()
        except Exception, e:
            print
            e
            self.db.rollback()
        return 0

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.zhihu.com/topic/19550517/top-answers', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a.question_link').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)
        for each in response.doc('div.zm-invite-pager span a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        items = response.doc('div.RichContent-inner>RichText CopyrightRichText-richText').items()
        if items == None:
            print 1
        title = response.doc('h1.QuestionHeader-title').text()
        html = response.doc('div.QuestionHeader-detail>RichText').html()
        if html == None:
            html = ''
        content = html.replace("'", "\\")
        qid = self.add_question(title,content,sum(1 for x in items))
        for each in response.doc('div.RichContent-inner>RichText CopyrightRichText-richText').items():
            self.add_comment(qid, each.html.replace('"', '\\"'))
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
