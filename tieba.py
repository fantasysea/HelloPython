__author__ = 'wuheyou'

import requests
head = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',

'Host':'tieba.baidu.com',
'Pragma':'no-cache',
'RA-Sid':'B70F1C2F-20140701-114416-cd78ab-ce789e',
'RA-Ver':'3.0.7',
'Referer':'https://www.baidu.com/link?url=AqlHUnCGiRUnATN43czWF_-LBDga5jFEvkwJ-Nc1UJUSpPUPPvpttm_xuDAEexADWTYOZ3sgZJIG_o6Fu9rYmq&wd=&eqid=fb166f5a0004755c0000000555d42cb6&tn=63090008_1_hao_pg',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}
cookie ={'Cookie':'TIEBA_USERTYPE=181e554047068cfd8f29bd97; bdshare_firstime=1418988694582; BDUSS=Dg3ek9IZkQ4MkNFOW5ONEZkdG9FbEJoMkxwT3J0Y0F-cDJtbElWaWVBMUlsUjlWQVFBQUFBJCQAAAAAAAAAAAEAAAATlbUHy6--9bXEtPPM4cfZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgI-FRICPhUa; TIEBAUID=9ad470692363ff906c1b1f52; BAIDUID=C1E7BF96A9290E494D0618158AB8FC20:FG=1; PSTM=1433402977; BIDUPSID=15D186F41C2064C914F91788683E980B; PRY=1; BDRCVFR[QehnocNy8Y6]=mEIYYlSGexffjm1njbsnj03g17xpA7E; BDRCVFR[JJAyrzZm4Kt]=I67x6TjHwwYf0; locale=zh; MCITY=-55%3A; BDRCVFR[Y7OWRVY3J9s]=I67x6TjHwwYf0; GET_TOPIC=129340691; LONGID=129340691; H_PS_PSSID=14666_1426_7477_12868_16800_16425_16514_15763_11773_13932_14551_16867'}
url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%9D%8E%E6%AF%85&fr=search'
html = requests.get('http://jp.tingroom.com/yuedu/yd300p')
html.encoding='utf-8'
# html = requests.get(url,headers=head,cookies=cookie)
print html.text
