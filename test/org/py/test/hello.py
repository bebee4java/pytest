#!/usr/bin/python
import sys
import random

# -*- coding: utf8 -*-

print("hello python")
print("你好")

# 注释以 # 开头

if True:
    print("True")
else:
    print("False")
print("end")

# python中单引号和双引号使用完全相同

# 自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行
s1 = r"this is a line with \n."
s2 = 'this is a line with \n.'
# python允许处理unicode字符串，加前缀u或U
s3 = u"this is an unicode string:中国"
print(s1); print(s2); print(s3)
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(word + '\n' + sentence + '\n' + paragraph)

x = 'runoob'
sys.stdout.write(x + '\n')

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
x = "x"; y = "y"
print(x); print(y)
print('===================')
print(x, end=""); print(y, end="")
print("===================")
print(sys.argv)
print(sys.path)

# reverse=True 降序
# a降序 b,c升序
data = list()
data.append({'a': 1, 'b': 2, 'c': 2})
data.append({'a': 3, 'b': 2, 'c': 3})
data.append({'a': 2, 'b': 3, 'c': 5})
data.append({'a': 1, 'b': 4, 'c': 2})
data.sort(key=lambda x: (x['a'], -x['b'], -x['c']), reverse=True)
for d in data:
    print(d)

print(3 > 4 < 5 > 9)    # 相当于(3>4) and (4<5) and (5<9) 如果遇到false直接false
