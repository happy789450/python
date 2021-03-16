# 模块的定义：
# 在python当中 一个.py文件就是一个模块
# 作用：
# 可以使我们有逻辑的去组织我们的python代码
# 以库的形式去封装功能，非常方便的去调用者去使用
# 可以定义函数 类 变量 也能包含可执行的代码
# 注意：不同的模块可以定义相同的变量名，但是每个模块中的变量名作用域只是在本模块中
#
# 模块分类：
# 内置模块 自定义的模块 第三方模块

#模块的制作说明
# __all__魔术变量的作用是 如果在一个文件中存在__all__变量，
# 那么也就意味这这个变量中的元素
# 会被from xxx  import * 时会被导入,对于import 方式来讲，无所谓， 有没有都可以全部的引用
__all__=['add','diff']
def add(x,y):
    '''
    普通的函数
    :param x:
    :param y:
    :return:
    '''
    return x+y

def diff(x,y):
    return x-y
def printInfo():
    return '这是我自定义模块里面的方法'

# 测试
if __name__=='__main__':
    res=add(2,5)
    # print('测试模块，%s'%res)
    print('模块__name__变量=%s'%__name__)