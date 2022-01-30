# 1).连接到数据库（host:localhost username:root password:root database:books autocommit:True）
# 2).把图书名称为‘西游记’的阅读量加一

# 导包
import pymysql

# 获取数据库连接
conn = pymysql.connect(host="api.mypeng.site", user="root", passwd="Lemon123456!", database="books", port=3306,
                       autocommit=True)

# 获取游标对象
cursor = conn.cursor()

# 执行操作
# 2).把图书名称为‘西游记’的阅读量加一
sql = "UPDATE t_book SET `read`=`read`+1 WHERE title='西游记'"
cursor.execute(sql)


# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
