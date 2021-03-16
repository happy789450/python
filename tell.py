#tell 返回指针当前所在的位置
# with open('test.txt','r') as f:
#     print(f.read(3))
#     print(f.tell())
#     print(f.read(2))
#     print(f.tell())
#truncate 可以对源文件进行截取操作
# fobjB=open('test2.txt','r')
# print(fobjB.read())
# fobjB.close()
# print('截取之后的数据......')
#
# fobjA=open('test2.txt','r+')
# fobjA.truncate(15)
# print(fobjA.read())
# fobjA.close()

#seek 可以控制光标所在的位置
# with open('test.txt','r')as f:
#     data=f.read(2)
#     # print(data.decode('gbk'))
#     f.seek(-2,1)#相当于光标设置到了0的位置
#     print(f.read(4).decode('gbk'))
#     f.seek(-6,2)#2 表示光标在末尾处 往回移动了6个字符
#     print(f.read(4).decode('gbk'))
