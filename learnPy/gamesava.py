# -*- coding:utf-8 -*-
import time, threading,os,shutil,sys

reload(sys)
sys.setdefaultencoding('utf8')
# 新线程执行的代码:
def loop(str1,str2):
    while True:
        shutil.copytree(str1,os.path.join(str2,time.strftime('%Y-%m-%d %Hh%Mm',time.localtime(time.time()))))
        time.sleep(600)

if __name__ == '__main__':
    str1 = "C:\\Program Files (x86)\\Steam\userdata\\140280942\\262060\\remote"
    str2 = "C:\\Users\\asus\\Desktop\\game\\darkest"
    # t = threading.Thread(target=loop(),name='LoopThread')
    # t.start()
    loop(str1,str2)
