import requestsTest
from bs4 import BeautifulSoup
import random
import re
def qiushibaike():
    content = requestsTest.get('http://www.qiushibaike.com')
    print type(content)
    # content = requests.get('http://www.qiushibaike.com').content
    # soup = BeautifulSoup(content,'html.parser')
    # for div in soup.find_all('div',{'class':'content'}):
    #     print div.text.strip()

if __name__ == '__main__':
    qiushibaike()