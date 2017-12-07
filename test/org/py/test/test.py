from collections import deque
l = ['s', 'v']
c = l.count('t')
print(c)

stack = list()
stack.append('3')
stack.append('1')
stack.pop()
print(stack)


queue = deque()
queue.append('3')
queue.append('1')
queue.popleft()
print(queue)


vec = [2, 4, 6]
vec = [3*x for x in vec]
print(vec)

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
print(matrix)
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

print(1, 2, 3, sep='|')

count = 0
while count < 5:
    print(count, " 小于 5")
    count += 1
else:
    print(count, " 大于或等于 5")

r = range(1, 20, 3)
print(r)
for i in range(1, 20, 3):
    print(i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i], sep=' = ')


def isprime(n):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
isprime(3)
isprime(349343)

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
