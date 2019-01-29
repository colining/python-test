import urllib2
import urllib


def demo1():
    request = urllib2.Request("http://www.baidu.com")
    response = urllib2.urlopen(request)
    print response.read()


def demo2():
    values = {"username": "rtq", "password": "86271325"}
    data = urllib.urlencode(values)
    url = "http://pt.cugb.edu.cn/login.php"
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    print response.read()
if __name__ == '__main__':
    # demo1()
    demo2()
