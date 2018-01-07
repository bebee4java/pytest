# 使用redis位图操作统计活跃用户数

import redis

r = redis.Redis(host='192.168.16.199', port=6379, db=0)

r.setbit('u1', 1, 1)
r.setbit('u1', 30, 1)

r.setbit('u2', 100, 1)
r.setbit('u2', 300, 1)

for i in range(3, 365, 3):
    r.setbit('u100', i, 1)

for i in range(4, 365, 2):
    r.setbit('u200', i, 1)

userList = r.keys('u*')
print(userList)

Au = []
Nau = []

for u in userList:
    loginCount = r.bitcount(u)
    if loginCount > 100:
        Au.append((u, loginCount))
    else:
        Nau.append((u, loginCount))
for uc in Au:
    print(str(uc[0]) + 'is a Active user.login count:' + str(uc[1]))
print('\n')
for uc in Nau:
    print(str(uc[0]) + 'is a Active user.login count:' + str(uc[1]))

