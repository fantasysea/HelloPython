__author__ = 'wuheyou'
# -*- coding: utf8 -*-
msg = u'今天天氣真好'
print msg
print u'字數:', len(msg)


# -*- coding: utf8 -*-
msg = '今天天氣真好'
print msg
print '字數:', len(msg)


# -*- coding: utf8 -*-
msg = u'今天天氣真好'
encoded = msg.encode('utf8')
print repr(encoded)


# -*- coding: utf8 -*-
encoded = '\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa4\xa9\xe6\xb0\xa3\xe7\x9c\x9f\xe5\xa5\xbd'
msg = encoded.decode('utf8')
print msg