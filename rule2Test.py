# * 匹配前一个字符出现0次或者无数次，即可有可无
import re
# res=re.match('[A-Z][A-Z]*','My')  #匹配0次
# res=re.match('[A-Z][a-z]*','Any') #匹配了2次
# res=re.match('[A-Z][a-z]*','AnyeverydayhappyIslaveer') #可以匹配无线次
# print(res.group())
# + 匹配前一个字符出现1次或者无限次，即至少有1次
# res=re.match('[a-zA-Z]+','MYNAMEisfjksg')
# 匹配符合规范 【规则是:不能以数字开头，只能包含字母，数字，下划线】的python变量名
# result=re.match('[a-zA-Z_]+[\w]*','name')
# result=re.match('[a-zA-Z_]+[\w]*','_name')
# result=re.match('[a-zA-Z_]+[\w]*','na99m_e')
# print(result.group())
# ? 告诉引擎匹配前导字符0次或者一次，事实上表示可选的
# result=re.match('[a-zA-Z]+[0-9]?','namefanck99m_e')
# print(result.group())
# {min,max} 告诉引擎匹配前导字符min次到max次，min和max必须是非负整数
# {count} 精确匹配
# {min,} max被省略的话表示max没有限制了
# result=re.match('\d{4,}','1234567890')
# result=re.match('\d{4,8}','123456789')
# if result:
#     print('匹配成功 {}'.format(result.group()))
# 匹配有限demo 格式xxxx@163.com
regexMail=re.match('[a-zA-Z0-9]{6,11}@163.com','sldjgfsdfosdfi@163.com')
if regexMail:
    print('匹配成功 {}'.format(regexMail.group()))
    pass