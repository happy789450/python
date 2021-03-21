# 通过python中re模块去学习并使用正则表达式的基本知识点
import re
data='Python is the best language in the word'
# result=re.match('y',data,re.I|re.M) #精确匹配 第三个参数表示忽略大小写
# print(type(result)) # 返回<class 're.Match'>
# print(result.group())
result = re.match('(.*) is (.*?) .*',data,re.I|re.M)
# group(num) 可以获取匹配的数据 如果有多个匹配结果的话 那么会以元组的形式 存放到group对象中，
# 此时我们可以通过下标去获取
if result:
    # print(result)
    print(result.groups(2))
    print(result.group(1))
    print(result.group(2))
    # print(result.group(3))
    print('匹配成功')
else:
    print(result.group())  # 如果匹配失败是没有group函数的 因为对象是空None
    print(result)
    print('匹配失败...')