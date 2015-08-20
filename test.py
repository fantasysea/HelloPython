__author__ = 'wuheyou'
import re

strs  = {"url": "http://o.wuheyou.com:88/user/signin", "json": "{\"ver\": \"1\", \"uuid\": \"000000000-000-000-0000-000000000\", \"sid\": \"diojl3eg3rk86sg3bl4dao1sa3\", \"mobile\": \"18680391276\", \"model\": \"iPhone5s\", \"type\": \" 5\", \"system\": \"1\", \"sv\": \"8.1\"}", "res_rc4": 1}
newstr = str(strs)
print newstr
result = re.findall("\"sid\": \"(.*?)\",",newstr)
for item in result:
    print item