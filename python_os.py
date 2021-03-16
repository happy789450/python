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
shutil.rmtree('/home/rice/test')