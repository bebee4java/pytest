#!/usr/bin/python3

c = input("请输入你要显示的斐波纳契数列数目：")
c = str(c)
if c.isdecimal():
    c = int(c)
else:
    print("输入有误，请检查！")
i = 0
a, b = 0, 1
while i < c:
    print(b)
    a, b = b, a+b
    i += 1

print('===================daemon 10=========================')
import sys


def fibonacci(n):   # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)   # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
