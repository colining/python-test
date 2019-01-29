# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import re
def regex():
    m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

    print "m.string:", m.string
    print "m.re:", m.re
    print "m.pos:", m.pos
    print "m.endpos:", m.endpos
    print "m.lastindex:", m.lastindex
    print "m.lastgroup:", m.lastgroup
    print "m.group():", m.group()
    print "m.group(1,2):", m.group(1, 2)
    print "m.groups():", m.groups()
    print "m.groupdict():", m.groupdict()
    print "m.start(2):", m.start(2)
    print "m.end(2):", m.end(2)
    print "m.span(2):", m.span(2)
    print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')
def demo1():
    request = urllib2.Request("http://www.baidu.com")
    response = urllib2.urlopen(request)
    print response.read()

def demo2():
    headers = {'User-Agent' : 'QQBrowser/9.6.11984.400','Referer':'http://pt.cugb.edu.cn/login.php','Host':'pt.cugb.edu.cn'}
    values = {'username': 'rtq', 'password': '86271325','logintype':'username','thispagewidth':'yes'}
    data = urllib.urlencode(values)
    url = "http://pt.cugb.edu.cn/takelogin.php"
    request = urllib2.Request(url,data,headers)
    try:
        response = urllib2.urlopen(request,timeout=10 )
        print response.read()
    except Exception ,e:
        print e

def demo3():
    req = urllib2.Request('http://blog.csdn.net/cqcre')
    try:
        urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.code
        print e.reason

def demo4():
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('https://www.baidu.com/')
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value
def demo5():
    # 设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 创建一个请求，原理同urllib2的urlopen
    response = opener.open("https://www.baidu.com/")
    # 保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

def demo6():
    filename = 'cookie.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({
        'stuid': '201200131012',
        'pwd': '23342321'
    })
    # 登录教务系统的URL
    loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
    # 模拟登录，并把cookie保存到变量
    result = opener.open(loginUrl, postdata)
    # 保存cookie到cookie.txt中
    cookie.save(ignore_discard=True, ignore_expires=True)
    # 利用cookie请求访问另一个网址，此网址是成绩查询网址
    gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
    # 请求访问成绩查询网址
    result = opener.open(gradeUrl)
    print result.read()
def demo7():
    filename = 'cookie.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # 利用cookie请求访问另一个网址，此网址是成绩查询网址
    gradeUrl = 'http://202.204.105.98/user/1004146111/home'
    # 请求访问成绩查询网址
    result = opener.open(gradeUrl)
    print result.read()
if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    regex()