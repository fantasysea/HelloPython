__author__ = 'wuheyou'
# coding=utf-8

import re
secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'

#
# a = 'xy123'
# b = re.findall('x.',a)
# print b

#
# a = 'xyxy123'
# b = re.findall("x*",a)
# print b

# a = 'xy1cvx23'
# b = re.findall('xy?',a)
# print b

# #.*的使用举例
# b = re.findall('xx.*xx',secret_code)
# print b
# # #.*？的使用举例
# c = re.findall('xx.*?xx',secret_code)
# print c

#
# d = re.findall('xx(.*?)xx',secret_code)
# print d
# for each in d:
#     print each


# s = '''sdfxxhello
# xxfsdfxxworldxxasdf'''
#
# d = re.findall('xx(.*?)xx',s,re.S)
# print d

#
# #对比findall与search的区别
# s2 = 'asdfxxIxx123xxlovexxdfddfxxyouxxd'
# f = re.search('xx(.*?)xx123xx(.*?)xx.*?xx(.*?)xx',s2)
# for item in f.groups():
#     print(item)
# # print f.group(2)
# f2 = re.findall('xx(.*?)xx123xx(.*?)xx',s2)
# print f2[0][1]


# s = '123rrrrr123'
# output = re.sub('123(.*?)123','123789d123',s)
# print output

# from re import findall,search,S
# info = findall('xx(.*?)xx',secret_code,S)
# for each in info:
#     print each


#不要使用compile
# pattern = 'xx(.*?)xx'
# new_pattern = re.compile(pattern,re.S)
# output = re.findall(new_pattern,secret_code)
# print output

#匹配数字
a = 'asdfasf1234567fasd555fas'
b = re.findall('(\d+)',a)
print b