# -*- coding:utf-8 -*-
print 'hello %d %d'%(1000,5)
classmates = ["小白","小红"]
print classmates[-2]
classmates.append("小黑")
print classmates[2]
classmates.pop()
print classmates[1]
print "------"
for name in classmates:
    print name
for i in range(1,5):
    print i
scores ={'小王': 5,'小红':6,}
print scores['小王']
help(abs)
scores.itervalues()
print [x*x for x in range(1,11)]

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
n = fib(100)
print n.next()
print n.next()
print n.next()
print n.next()
print n.next()
for i in  range(1,10):
    try:
        if(i%2 == 0):
            raise Exception("some wrong")
    except Exception ,e:
        continue
    print i
