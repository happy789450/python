import sys
import psutil
import os
import gc

print(gc.get_threshold())
# psutil.test()
def showMemSize(tag):
    pid=os.getpid()
    p=psutil.Process(pid)
    info=p.memory_full_info()
    memory=info.uss/1024/1024
    print('{} memory used:{} MB'.format(tag,memory))
    pass

# 验证循环引用的情况
def func():
    showMemSize('初始化')
    a=[i for i in range(10000000)]
    b=[i for i in range(10000000)]
    a.append(b)
    b.append(a)
    showMemSize('创建列表对象 a b 之后')
    # print(sys.getrefcount(a))
    # print(sys.getrefcount(b))
    # del a
    # del b
    pass
func()
gc.collect()
showMemSize('完成时候的')
# a=[]
# print(sys.getrefcount(a)) # 2次
# b=a
# print(sys.getrefcount(a)) # 3次
# c=b
# d=c
# e=d
# f=e
# g=f
# print(sys.getrefcount(a)) # 8次