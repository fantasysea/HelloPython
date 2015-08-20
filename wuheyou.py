__author__ = 'wuheyou'
# coding=utf-8
import requests
# import rc4
import rcc
import json

import re
head = {
   'Accept-Encoding':'gzip, deflate'
,
'Accept-Language':'zh-CN,zh;q=0.8'
,
'Cache-Control':'no-cache'
,
'Connection':'keep-alive'
,
'Content-Length':'395'
,
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
,
'Cookie':'sid=diojl3eg3rk86sg3bl4dao1sa3; token=YWE4Ym5EYkd2ZUszN1FTMUgzMTJKd3pwbHRCZlVmQVVybFRDUmhYV3dBOmE2NTZOaDhLV3B0cEN0OXVXVCt2S0M3RDVpc0dZOFg4dzdOanhOUU8rMHBXdEF6Q2tzS0toYXZDa1lNWGtMUVJUQlJ2RUM2ZTVLVnVoSHdBZ3c%3D; vector-nav-p-.E6.97.A0.E4.BD.95.E6.9C.89.E6.89.8B.E6.9C.BA.E7.AB.AF=true; vector-nav-p-.E5.85.AC.E5.8F.B8.E5.8A.9E.E5.85.AC.E8.AE.BE.E7.BD.AE=true; vector-nav-p-tb=true'
,
'Host':'www.wiki.com'
,
'Origin':'http'
,
'Pragma':'no-cache'
,
'Referer':'http'
,
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
,
'X-Requested-With':'XMLHttpRequest'
}

cookie = {'sid':'915t8ilupt2nurdmpb0stl11f4,',
          'vector-nav-p-.E5.85.AC.E5.8F.B8.E5.8A.9E.E5.85.AC.E8.AE.BE.E7.BD.AE':'true',
          'vector-nav-p-.E5.85.AC.E5.8F.B8.E5.8A.9E.E5.85.AC.E8.AE.BE.E7.BD.AE':'true',
          'vector-nav-p-tb':'true',
          'token':'MWUxMUZzcUpXTzNaNnMrWmc0Wmt4d3dIV2MyVkdPcFg3RWxaTmNZRnlnOjkwOTZnQmFmbnZ3Y0ZaemI3aktRVlpPYTltdGFzcXV2T3NJaUMyWkk2RDVLaTBMdVpYeGdTam5TaGtRTVIxZ1B5eVlNdTNkSzRVQkZobjIvWlE%3D'}


#
# cookie ={'Cookie':'TIEBA_USERTYPE=181e554047068cfd8f29bd97; bdshare_firstime=1418988694582; BDUSS=Dg3ek9IZkQ4MkNFOW5ONEZkdG9FbEJoMkxwT3J0Y0F-cDJtbElWaWVBMUlsUjlWQVFBQUFBJCQAAAAAAAAAAAEAAAATlbUHy6--9bXEtPPM4cfZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgI-FRICPhUa; TIEBAUID=9ad470692363ff906c1b1f52; BAIDUID=C1E7BF96A9290E494D0618158AB8FC20:FG=1; PSTM=1433402977; BIDUPSID=15D186F41C2064C914F91788683E980B; PRY=1; BDRCVFR[QehnocNy8Y6]=mEIYYlSGexffjm1njbsnj03g17xpA7E; BDRCVFR[JJAyrzZm4Kt]=I67x6TjHwwYf0; locale=zh; MCITY=-55%3A; BDRCVFR[Y7OWRVY3J9s]=I67x6TjHwwYf0; GET_TOPIC=129340691; LONGID=129340691; H_PS_PSSID=14666_1426_7477_12868_16800_16425_16514_15763_11773_13932_14551_16867'}
# url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search'


data = {
    "ver": "1.1",
    "type": 1,
    "mobile": "15827636145",
    "password": "4297f44b13955235245b2497399d7a93"
}



signin = {
   "sid": "diojl3eg3rk86sg3bl4dao1sa3",
   "system": "1",
   "mobile": "18680391276",
   "ver": "1",
   "model": "iPhone5s",
   "uuid": "000000000-000-000-0000-000000000",
   "sv": "8.1",
  "type":" 5"
}

data2 = {
    'url':'http://o.wuheyou.com:88/user/signin',
    'json':json.dumps(signin),
    'res_rc4':1
}

print json.dumps(data2)


url2 = 'http://www.wiki.com/wuheyou_test/api.php'
html = requests.post(url2,data=data2,headers = head)
print html.text




login = {
    'system':1,
    "ver": "1.2.1",
    "type": 1,
    "mobile": "15816860185",
    "password": "e10adc3949ba59abbe56e057f20f883e"
}



'''模拟登录成功


'''
url = 'http://o.wuheyou.com:88/user/login'
# rc = rc4("2*s&3Hd#kd90")
# str = rc.encode(login)
str = rcc.rc4(json.dumps(login), "2*s&3Hd#kd90", 0)
# print str
url = 'http://o.wuheyou.com:88/user/login'
# result = requests.post(url,data=str)
# print  rcc.rc4(result.text, "2*s&3Hd#kd90", 0)
# print  rcc.rc4(result.content, "2*s&3Hd#kd90", 0)


'''获取个人资料


'''

medalrank = {
    "sid": "p5ir1otumv71bcd6fauqd8e9o1",
    "system": "1",
    "mobile": "13267180788",
    "ver": "1",
    "model": "x86_64",
    "uuid": "000000000-000-000-0000-000000000",
    "sv": "8.1",
    "type": 5
}
# rc = rc4("2*s&3Hd#kd90")
# str = rc.encode(login)
str = rcc.rc4(json.dumps(medalrank), "2*s&3Hd#kd90", 0)
print json.dumps(medalrank)
url = 'http://o.wuheyou.com:88/user/getselfinfo'
result = requests.post(url,data=str)
print  result.content
# print  rcc.rc4(result.content, "2*s&3Hd#kd90", 0)

