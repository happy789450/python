import sys
import argparse
# print('参数个数为:',len(sys.argv),'个参数.')
# print('参数列表:',str(sys.argv[1:]))

# 创建一个解析器对象
parse=argparse.ArgumentParser(prog='my - program', usage='%(prog)s [options] usage',
                              description = 'my-编写自定义命令行的文件',epilog = 'my -epilog')
# 添加位置参数【必选参数】
parse.add_argument('name',type=str, help='你自己的名字')
parse.add_argument('age',type=str,help='你的年龄')

# 添加可选参数
# parse.add_argument('-s','--sex',action='append', type=str,help='你的性别')
# 限定一个范围
parse.add_argument('-s','--sex',default='男',choices=['男','女','male','female'], type=str,help='你的性别')

# print(parse.print_help())
result=parse.parse_args() # 开始解析参数
print(result.name,result.age,result.sex)