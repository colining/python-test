# -*- coding:utf-8 -*-
from pyquery import PyQuery as pq

if __name__ == '__main__':
    text = unicode(open('v2ex.html').read(), "utf-8")
    p = pq(text)
    print p('h2').html()
    for each in p('div.inner>a').items():
        if each.attr.href.find('tab') >0:
            print 1,each.attr.href

    # for each in q('#Tabs>a').items():
    #     print 2,each.attr.href
    #
    # for each in q('.cell>a[href^="/go/"]').items():
    #     print 3,each.attr.href
    #
    # for each in q('.cell a[href^="/go/"]').items():
    #     print 4,each.attr.href
    #
    # for each in q('span.item_title>a').items():
    #     print 5,each.html()


