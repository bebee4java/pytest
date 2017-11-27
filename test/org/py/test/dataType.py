#!/usr/bin/python3
counter = 100 #整型变量
miles = 1000.0 #浮点型变量
name = 'runoob' #字符串
print(counter)
print(miles)
print(name)

a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, "runoob"
print(a, b, c)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))
print('==========class============')
class A:
    pass
class B(A):
    pass
print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)
