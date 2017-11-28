#!/usr/bin/python3
counter = 100       # 整型变量
miles = 1000.0      # 浮点型变量
name = 'runoob'     # 字符串
print(counter)
print(miles)
print(name)

a = b = c = 1
print(a, b, c)
# 同时给多个变量赋值
a, b, c = 1, 2, "runoob"
print(a, b, c)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))
print('==========class============')


class A:
    pass    # Python pass是空语句，是为了保持程序结构的完整性。不做任何事情，一般用做占位语句


class B(A):
    pass
# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型
print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)
print('===========True False=============')
print(True + 4)     # True=1
print(False + 4)    # False=0

print('=============运算==================')
print(2 / 4)    # 除法，等到一个浮点数
print(2 // 4)   # 除法，等到一个整数
print(17 % 3)   # 取余
print(2 ** 5)   # 乘方

print('================string===================')
str = 'Runoob'
# 索引值以 0 为开始值，-1 为从末尾的开始位置
print(str)              # 输出字符串
print(str[0:-1])        # 输出第一个到倒数第二个的所有字符
print(str[0])           # 输出字符串第一个字符
print(str[2:5])         # 输出从第三个开始到第五个的字符
print(str[2:])          # 输出从第三个开始的后的所有字符
print(str * 2)          # 输出字符串两次
print(str + "TEST")     # 连接字符串
print(str[-1])          # 倒数第一个字符
# Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误
# str[0] = 's'

print('==================list=======================')
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
del tinylist[0]
print(tinylist)

print(list)             # 输出完整列表
print(list[0])          # 输出列表第一个元素
print(list[1:3])        # 从第二个开始输出到第三个元素
print(list[2:])         # 输出从第三个元素开始的所有元素
print(tinylist * 2)     # 输出两次列表
print(list + tinylist)  # 连接列表
# 与Python字符串不一样的是，列表中的元素是可以改变的
list[0] = 's'
print(list)
list[1:3] = ['1', '2', '3']
print(list)
list.append("aaaaa")
print(list)
print('======================Tuple===========================')
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)                # 输出完整元组
print(tuple[0])             # 输出元组的第一个元素
print(tuple[1:3])           # 输出从第二个元素开始到第三个元素
print(tuple[2:])            # 输出从第三个元素开始的所有元素
print(tinytuple * 2)        # 输出两次元组
print(tuple + tinytuple)    # 连接元组
# tuple[0] = '3' ->error    # 与字符串一样，元组的元素不能修改

tup1 = ()     # 空元组
print(tup1)
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup2)

print('==========================set=================================')
# 集合（set）是一个无序不重复元素的序列
# 基本功能是进行成员关系测试和删除重复元素
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
set1 = set()
print(set1)
parame = {'s', 'e', 't'}
print(parame)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')


# set可以进行集合运算
a = set('abracadabra')   # 转换为可变集合
b = set('alacazam')

print(a)

print(a - b)     # a和b的差集

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素

print('===================Dictionary==============================')
'''
列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合
键(key)必须使用不可变类型
在同一个字典中，键(key)必须是唯一的
'''
d = {}
d['one'] = "1 - 菜鸟教程"
d[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(d['one'])         # 输出键为 'one' 的值
print(d[2])             # 输出键为 2 的值
print(tinydict)            # 输出完整的字典
print(tinydict.keys())     # 输出所有键
print(tinydict.values())   # 输出所有值

d = dict(Runoob=1, Google=2, Taobao=3)
print(d)

# 遍历字典
for c in d:
    print(c, ':', d[c])

d.clear()
print(d)

print('=====================type convert=======================')
i = complex(1, 2)
j = complex(2, 3)
print(i + j)
str = '7+4'
print(eval(str))




