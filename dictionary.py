__author__ = 'wuheyou'

from Stack import Stack

d = ["aaa","dff","cccc",("dd","ddd")]
# print(d[len(d)-1])
print(d[-1])
print(d[3])
del d[-1]
del d[-1]
del d[-1]
print(d[-1])



for item in d:
    print(item)

s = Stack(10)
for name in range(0,11):
    s.push("aa {0}".format(name))


s.out()

print(s.Full())

di = {"zhaoliu":"aaa","wangwu":"dff","lisi":"cccc","zhangsan":("dd","ddd")}

print(di["zhaoliu"])

for item in di:
    print(di[item])


for item in [1,2,3,4,6]:
    print(item)

print(range(1,100,1))