# 1).连接到数据库（host:localhost username:root password:root database:books autocommit:True）
# 2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）

# 导包
import pymysql

# 获取数据库连接
conn = pymysql.connect(host="8.131.250.56", user="root", passwd="password", database="books", port=3306,
                       autocommit=True)

# 获取游标对象
cursor = conn.cursor()

# 执行操作
# 2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
# sql = "insert into t_book(id,title,pub_date) values(4, '西游记', '1986-01-01')"
sql = "insert into t_book(title,pub_date) values('西游记', '1986-01-01')"
cursor.execute(sql)

print("rowcount==", cursor.rowcount)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
