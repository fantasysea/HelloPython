__author__ = 'wuheyou'
__author__ = 'CC'
# coding=utf-8
# -*- coding: utf8 -*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# r = requests.get("http://www.baidu.com/")
# r.encoding = 'utf-8'
# print r.content

class spider:
    def getHtml(self,url):

        return requests.get(url)

    def getItem(self,html):
        item = {}
        item['title'] = re.findall('title="(.*?)" ',html,re.S)[0]
        item['content'] = re.findall('none;">(.*?)</p>',html,re.S)[0]
        cf = re.findall('<em>(.*?)</em>',html,re.S)
        item['time'] = cf[0]
        item['xinhao'] = cf[1]
        item['number'] = re.findall('learn-number">(.*?)</em>',html,re.S)[0]
        return item

    def saveItem(self,item):
        f = open('info.txt','a')
        f.writelines(item['title'].strip('\r\n\t') + '\n')
        f.writelines(item['content'].strip('\r\n\t') + '\n')
        f.writelines(item['time'].strip('\r\n\t') + '\n')
        f.writelines(item['xinhao'].strip('\r\n\t') + '\n')
        f.writelines(item['number'].strip('\r\n\t') + '\n')



if __name__=='__main__':

    url = 'http://www.jikexueyuan.com/course/?pageNum=2'
    jikespider = spider()
    html = jikespider.getHtml(url)
    html.encoding = 'utf-8'
    print html.text
    list = re.findall('deg=\"0\" >(.*?)</li>',html.text,re.S)
    print list
    for each in list:
        item = jikespider.getItem(each)
        print item
        jikespider.saveItem(item)
        print item['title'].strip('\r\n\t')
        print item['content'].strip('\r\n\t')
        print item['time'].strip('\n\t')
        print item['xinhao'].strip('\r\n\t')
        print item['number'].strip('\r\n\t')
