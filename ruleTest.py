# . 点的使用 匹配规则是除了 换行符之外的任意字符
import re
# data='a1aaa'
# names='李达','李明','小王','小李'
# pattern='李.'
# # parrtern='...'
# for name in names:
#     res=re.match(pattern,name)
#     if res:
#         print(res.group())
# []中括号的使用  匹配规则是:匹配中括号中的任意一个字符
# str1='eee'
# res=re.match('[He]',str1)
# print(res.group())
# pattern='[abc]'  # 使用中括号括起来的内容，代表一个集合，代表匹配集合内的任意一个字符
# 【abc】代表可以匹配a或者b或者c
# pattern='[a-z]' #可以简写一个范围abcde...
# datas='a','b','c','e','wyw'
# for data in datas:
#     result=re.match(pattern,data)
#     if result:
#         print('匹配成功 %s'%result.group())

# \d 匹配一个数字 0-9
# data='12345abcdef'
# print(re.match('\d\d\d',data).group())
# \D 匹配一个非数字
# data='w12345abcdef'
# print(re.match('\D',data).group())
#\s 匹配一个空白字符 或者tab键
# data='  hello'
# print(re.match('\s\s',data).group())
# \S 匹配非空白字符
# data='Python hello'
# print(re.match('\S\S\S\S\S\S',data).group())
# \w 匹配单词字符，即a-z A-Z 0-9 _
# data='_2Yssdf'
# print(re.match('\w\w',data).group())
# \W 匹配非单词的字符
# data='@$#  _2Yssdf'
# print(re.match('\W\W',data).group())