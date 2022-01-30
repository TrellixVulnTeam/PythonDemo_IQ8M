# 1).连接到数据库（host:localhost username:root password:root database:books autocommit:True）
# 2).删除名称为‘西游记’的图书

# 导包
import pymysql

# 获取数据库连接
conn = pymysql.connect(host="api.mypeng.site", user="root", passwd="Lemon123456!", database="books", port=3306,
                       autocommit=True)

# 获取游标对象
cursor = conn.cursor()

# 执行操作
sql = "DELETE FROM t_book WHERE title='西游记';"
cursor.execute(sql)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
