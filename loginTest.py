import sys
import argparse
# print('参数个数为:',len(sys.argv),'个参数.')
# print('参数列表:',str(sys.argv[1:]))

# 创建一个解析器对象
parse=argparse.ArgumentParser(prog='系统登录', usage='%(prog)s [options] usage',
                              description = '系统登录自定义命令行的文件',epilog = 'my -epilog')
# 添加位置参数【必选参数】
parse.add_argument('loginType',type=str, help='登录系统类型')
# 添加可选参数
parse.add_argument('-u',dest='user', type=str,help='你的用户名')
parse.add_argument('-p',dest='pwd', type=str,help='你的密码')

# print(parse.print_help())
result=parse.parse_args() # 开始解析参数
if (result.user=='root' and result.pwd=='123456'):
    print('login success!')
else:
    print('login fail')