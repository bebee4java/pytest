#!/usr/bin/python3
from isNum import is_number
import isNum
print('请输入要计算的两个数值和运算符：')
x = input("x :")
p = input("操作符 :")
y = input("y :")
if isNum.is_number(x) and is_number(y):
    if '+' == p:
        print("%.2f + %.2f = %.2f" % (float(x), float(y), float(x)+float(y)))
    elif '-' == p:
        print("%.2f - %.2f = %.2f" % (float(x), float(y), float(x)-float(y)))
    elif '*' == p:
        print("%.2f * %.2f = %.2f" % (float(x), float(y), float(x)*float(y)))
    elif '/' == p:
        print("%.2f / %.2f = %.2f" % (float(x), float(y), float(x)/float(y)))
    else:
        print("不认识的操作符")
else:
    print("data type error")
