__author__ = 'wuheyou'
#coding=utf-8
import requests
import json

data = {
'mobile':'weishaoyin@163.com',
'password_5292':'fantasyweibo',
'remember':'on',
'backURL':'http%3A%2F%2Fweibo.cn',
'backTitle':'手机新浪网',
'tryCount':'',
'vk':'5292_302b_1969177596',
'submit':'登录'
}
url = 'http://login.weibo.cn/login/?rand=750225239&backURL=http%3A%2F%2Fweibo.cn&backTitle=%E6%89%8B%E6%9C%BA%E6%96%B0%E6%B5%AA%E7%BD%91&vt=4'
html = requests.post(url,data=json.dump(data))
print html.text
