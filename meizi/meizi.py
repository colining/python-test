# coding:utf-8
import requests
from pyquery import PyQuery
import re
import urllib
import urllib2
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#通过主页导航，获取链接集合
def getPicture():
    url = "http://www.mmjpg.com/tag/meixiong"
    r = requests.get(url, proxies = getProxy(), headers=getHeaders());
    r.encoding = 'utf8'
    q = PyQuery(r.text)
    myList = list()
    for each in q('body > div.main.topno > div.pic > ul > li>a').items():
        myList.append(each.attr.href)
        # print each.attr.href
    for href in myList:
        downLoad(href)


def downLoad(href):
    r = requests.get(href, getHeaders())
    r.encoding = 'utf8'
    q = PyQuery(r.text)
    #该链接下的图片总数
    total = int(q('#page > a:nth-child(9)').text())
    #该链接下的标题，用来创建文件夹
    title = q('body > div.main > div.article > h2').text()
    href = q('div.content > a> img').attr.src[0:-5]
    dirName = u"【{}P】{}".format(total, title)
    # 定义要创建的目录
    mkpath = "c:\\mymeizi\\" + dirName + "\\"
    # print mkpath
    # 调用函数
    # print  href
    if makedir(mkpath):
        print mkpath + "目录已创建"
        for x in range(1, total + 1):
            try:
                imgurl = href + str(x) + ".jpg"
                # urllib.urlretrieve(imgrul, mkpath + "/%s.jpg" % x)
                # opener = urllib2.build_opener()
                # opener.addheaders = [('Host','img.mmjpg.com'),
                #                              ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                #                                             'Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'),
                #                              ('Referer','http://www.mmjpg.com/mm')]
                # urllib2.install_opener(opener)
                # urllib2.urlretrieve(imgurl, mkpath + "/%s.jpg" % x)
                # os.chdir(r"D:")
                # header = {
                #     'Host': 'img.mmjpg.com',
                #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                #                   'Chrome/59.0.3071.115 Safari/537.36',
                #     'Referer': 'http://www.mmjpg.com/mm/1188/3'
                # }
                # request = urllib2.Request(imgurl, None, header)
                # response = urllib2.urlopen(request)
                # f = open(name, 'wb')
                # f.write(response.read())
                # f.close()
                # print(imgurl)
                # print href + str(x) + ".jpg"
                # print imgurl
                headers = {
                    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
                    'Accept - Encoding': 'gzip, deflate, sdch',
                    'Accept - Language': 'zh - CN, zh;q = 0.8',
                    'Cache - Control': 'max - age = 0',
                    'Connection': 'keep - alive',
                    'DNT': '1',
                    'Host': 'img.mmjpg.com',
                    'Referer': 'http: // www.mmjpg.com',
                    'Upgrade - Insecure - Requests': '1',
                    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 53.0.2785.104 Safari / 537.36 Core / 1.53.3427.400 QQBrowser / 9.6.12513.400',
                }
                print imgurl
                r = requests.get(imgurl,headers = headers)
                print r.status_code
                with open(mkpath + "/%s.jpg" % x,"wb") as code:
                    code.write(r.content)
                # data = urllib.urlopen(imgurl).read()
                # f = file(mkpath + "/%s.jpg" % x, "wb")
                # f.write(data)
                # f.close()
            except Exception,e:
                print "出了一点小小的错误"
                continue

def makedir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print path + ' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + ' 目录已存在'
        return False

def getHeaders():
    # headers = {
    #     'Host': 'www.mmjpg.com',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                   'Chrome/59.0.3071.115 Safari/537.36',
    #     'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
    # }
    headers = {
        'Host': 'www.mmjpg.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Referer':'http://www.mmjpg.com'
    }
    return headers


def getProxy():
    proxies = {"http": "http://223.215.43.110:8090"}
    # # proxies = {"http": "http://60.255.186.169:8888"}
    # r=requests.get("http://ip.chinaz.com/getip.aspx", proxies=proxies)
    # print r.text
    # return proxies
    return
if __name__ == '__main__':
    getPicture()
    # getProxy()
