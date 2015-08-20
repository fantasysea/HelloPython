__author__ = 'wuheyou'
#-*_coding:utf8-*-

import re
import requests
# head = {'content-length': '51213', 'via': 'ZJHZ_237_75 (DLC-3.0), gdad_249_202 (DLC-3.0)', 'content-encoding': 'gzip', 'age': '2096963', 'expires': 'Tue, 25 Aug 2015 00:39:40 GMT', 'vary': 'Accept-Encoding', 'server': 'DnionOS/1.2.1.3', 'last-modified': 'Thu, 11 Jun 2015 18:52:39 GMT', 'connection': 'keep-alive', 'etag': 'W/"5579d8f7-c9d5"', 'cache-control': 'max-age=2592000', 'date': 'Sat, 08 Aug 2015 18:29:37 GMT', 'content-type': 'text/html'}
# html = requests.get("http://www.jikexueyuan.com/",headers = head)
# print html


f = open("jike",'r')
html = f.read()
f.close()
# print html

print 'hello world'
for i in range(10):
    a = i
    print a

imges = re.findall("<img src=\"(.*?)\" class=\"lesso",html)
i = 0;
for image in imges:
    print image
    '''正则表达式 打印获取图片的名字

    \Z是结尾的意思'''
    print re.findall("/(\w+\.\w+\Z)",image)[0]
    f2 = open("images/"+re.findall("/(\w+\.\w+\Z)",image)[0],'wb')
    imagedata = requests.get(image)
    print imagedata.status_code
    print imagedata.cookies
    print imagedata.headers
    f2.write(imagedata.content)
    f2.close()
    i = i+1