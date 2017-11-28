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
