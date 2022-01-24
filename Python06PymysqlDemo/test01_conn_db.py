# 1).连接到数据库（host:localhost username:root password:root database:books）
# 2).获取数据库服务器版本信息

# 导包
import pymysql

# 获取数据库连接
conn = pymysql.connect(host="8.131.250.56", user="root", passwd="passwordMYSQL123", database="books", port=3308)

# 获取游标对象
cursor = conn.cursor()

# 执行操作：获取数据库服务器版本信息
cursor.execute("SELECT VERSION()")

# 获取查询结果
result = cursor.fetchone()
print("result=", result)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
conn.close()
