__author__ = 'wuheyou'
# coding=utf-8
import requests
import re
'''处理headers的文件


'''

f = open("headers.txt",'r')
lingg = f.readline().strip()
for line in f.readlines():
    line = line.strip()
    list = line.split(':')
    newline = '\''+list[0]+'\''+":"+'\''+list[1]+'\''
    print newline
    print ","

