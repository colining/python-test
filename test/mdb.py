#!/usr/bin/env python
# coding=utf-8

import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect('127.0.0.1', 'root', '86271325', 'wenda', charset='utf8')
    try:
        cursor = db.cursor()
        # sql = 'insert into question (title,content,user_id,created_date,comment_count)VALUES ("xxx","xxx",1,now(),0)'
        # cursor.execute(sql)
        # qid = cursor.lastrowid
        # print qid
        # db.commit()
        sql = 'select * from question order by id DESC  limit 2'
        cursor.execute(sql)
        for each in cursor.fetchall():
            for row in each:
                print row
        db.commit()
    except Exception, e:
        print e
        db.rollback()
    db.close


def __init__(self):
    self.db = MySQLdb.connect('localhost', 'root', 'root', 'wenda', charset='utf8')


def add_question(self, title, content):
    try:
        cursor = self.db.cursor()
        sql = 'insert into question(title, content, user_id, created_date, comment_count) values ("%s","%s",%d, %s, 0)' % (
            title, content, random.randint(1, 10), 'now()');  # 插入数据库的SQL语句
        print sql
        cursor.execute(sql)
        print cursor.lastrowid
        self.db.commit()
    except Exception, e:
        print e
        self.db.rollback()
