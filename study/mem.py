# a=140
# b=140
# print(id(a))
# print(id(b))
# del a
# del b
# c=140
# print(id(c))

biga=10000
bigb=10000
print(id(biga))
print(id(bigb))
del biga
del bigb
bigc=10000
print(id(bigc))
# 大整数池和小整数池的区别是：
# 1 从结果来看是一样的
# 2 大整数池是没有提前创建好对象， 是个空池子，需要我们自己去创建
# 创建好之后，会把整数对象保存到池子里面，后面都是不需要创建了 直接拿过来使用
# 小整数池是提前将 【-5，256】的数据都是提前创建好