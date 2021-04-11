from moduleTest import mokuai

# from mokuai import add  #第二种导入方式
# from mokuai import *    #第三种导入方式
# res=mokuai.add(1,3)
# print(mokuai.diff(7,4))
# print(res)
# print(add(67,3))
# print(diff(12,2))
# print(printInfo()) #对于这种情况就不能使用了 因为没有在__all__中
print(mokuai.printInfo()) #尽管不在__all__中 也可以调用