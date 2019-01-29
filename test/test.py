import requests
from bs4 import BeautifulSoup
import random
import re
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content,'html.parser')
    for div in soup.find_all('div',{'class':'content'}):
        print div.text.strip()

def demo_string():
    stra = 'hello world'
    strb = 'hello world'
    strc = '\n\r hello world \r\n'
    print stra.replace('world','nowcoder')
    print stra
    print strc.lstrip()
    print 5,strc.startswith('x')
def demo_obj():
    user1 = User('jim',1)
    print user1
    guest = Guest("guest",2)
    print guest
    admin =Admin('lalal',1,2)
    print Admin
class User:
    type = 'User'
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im' + self.name + ' '+ str(self.uid)

class Guest(User):
    def __repr__(self):
        return 'im guest' + self.name + '  '+ str(self.uid)

class Admin(User):
    type = 'Admin'
    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group = group
    # def __repr__(self):
    #         return 'im admin' + self.name + ' ' + str(self.uid) +' '+str(self.group)
def demo_exception():
    try:
        2/0
    except Exception as e:
        print  'error' ,e
    finally:
        print 'clean up'
def demo_random():
    # random.seed(1)
    for i in range(0,5):
        print random.randint(0,100)
    print random.random()
    print 3,random.choice(range(0,1000,5))
    print 4,random.sample(range(0,1000,5),4)

    lista = [1,2,3,4,5]
    random.shuffle(lista)
    print lista
def demo_regex():
    str = 'abc123def456'
    p1 = re.compile('[\d]')
    print 1 ,p1.findall(str)
    str1 = 'a@163.com,b@google.com,c@qq.com,d@qq.com,e@163.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 2,p3.findall(str1)
    str2 = '<html><h>title</h><body>content</body></html>'
    p4 = re.compile('<h>[<]+</h>')
    print 4,p4.findall(str2)
    str = 'xx2016-08-20zzz,xx2016-8-20zzz'
    p5 = re.compile('\d{4}-\d{1,2}-\d{2}')
    print 5, p5.findall(str)
if __name__ == '__main__':
    qiushibaike()
    # demo_string()
    # lista =[1,2,3,4,]
    # listb = [2,3,4,5]
    # lista = lista + listb
    # print lista
    # demo_obj()
    # demo_exception()
    # demo_random()
    # demo_regex()


