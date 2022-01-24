# 1).连接到数据库（host:localhost username:root password:root database:books）
# 2).查询图书表的数据（包括：图书id、图书名称、阅读量、评论量）
# 3).获取查询结果的总记录数
# 4).获取查询结果的第一条数据
# 5).获取全部的查询结果

# 导包
import pymysql

# 获取数据库连接
conn = pymysql.connect(host="8.131.250.56", user="root", passwd="passwordMYSQL123", database="books", port=3308)

# 获取游标对象
cursor = conn.cursor()

# 执行操作
# 2).查询图书表的数据（包括：图书id、图书名称、阅读量、评论量）
sql = "SELECT t.id,t.title,t.`read`,t.`comment` FROM t_book t"
cursor.execute(sql)

# 3).获取查询结果的总记录数
rowcount = cursor.rowcount
print("rowcount==", rowcount)

# 4).获取查询结果的第一条数据
# first = cursor.fetchone()
# print("first=", first)
# data = cursor.fetchone()
# print("data=", data)

# 5).获取全部的查询结果
data_list = cursor.fetchall()
print("data_list===", data_list)
for book in data_list:
    id, title, read, comment = book
    print("id={} title={} read={} comment={}".format(id, title, read, comment))

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
