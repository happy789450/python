import os
import shutil
# os.rename('test2.txt','test3.txt')
# os.remove('test3.txt') #删除文件，前提是文件存在
# os.mkdir('test3')
# os.rmdir('test3')  #删除文件夹 文件夹必须存在
# os.mkdir('/home/rice/test/')
# os.mkdir('/home/rice/test/test2') # 不允许创建多级目录
# os.makedirs('/home/rice/test/test2') # 创建多级目录
# os.rmdir('/home/rice/test') #只能删除空目录
#如果要删除非空目录 就需要调用shutil模块
# shutil.rmtree('/home/rice/test') #删除非空目录
# print(os.getcwd())
# 路径的拼接
# print(os.path)
# print(os.path.join(os.getcwd(),'venv'))
# listRs=os.listdir('/home/rice') #老版写法
# for dirname in listRs:
#     print(dirname)
# 现代版写法
# scandir 和with一起来使用 这样的话 上下文管理器会在迭代器遍历完成后自动
# 去释放资源
# with os.scandir('/home/rice') as entries:
#     for entry in entries:
#         print(entry.name)
# basePath='/home/rice/桌面'
# for entry in os.listdir(basePath):
#     # if os.path.isfile(os.path.join(basePath,entry)):
#     #     print(entry)
#     if os.path.isdir(os.path.join(basePath,entry)):
#         print(entry)