# 创建数据库的链接
from pymysql import *
conn=connect(host='10.4.45.2',user='root',password='123456',
             database='studb',charset='utf8')
# 创建一个游标对象 可以利用这个对象进行数据库的操作
try:
    cur=conn.cursor()
    insertsql='''
    insert into student(id,name,address) values (100,'张三','深圳')
    '''
    # cur.execute(insertsql)
    cur.execute('select * from student where id=%s',[100])
    # conn.commit()
    result=cur.fetchall()
    for item in result:
        print('姓名:{0} 地址:{1}'.format(item[1],item[4]))
    print('sucess')

except Exception as ex:
    print(ex)
    pass
finally:
    cur.close()
    conn.close()