#!/usr/bin/python3


# 打开一个文件
def writefile(file, content, charset):
    f = open(file, mode="w", encoding=charset)
    f.write(content)
    # 关闭打开的文件
    f.close()


def readfile(file, charset):
    f = open(file, mode="r", encoding=charset)
    str = f.read()
    f.close()
    return str

str = "你好 python"
writefile("C:\\Users\\Administrator\\Desktop\\filetest.txt", str, "utf-8")
s = readfile("C:\\Users\\Administrator\\Desktop\\filetest.txt", "utf-8")
print(s)
