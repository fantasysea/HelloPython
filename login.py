__author__ = 'wuheyou'

#coding=utf8

import httplib

httpClient = None

try:
    httpClient = httplib.HTTPConnection('baidu.com', 80, timeout=30)
    httpClient.request('GET', '/')

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()