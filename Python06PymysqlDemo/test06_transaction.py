# 1).连接到数据库（host:localhost user:root password:root database:books），并开启自动提交事务
# 2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
# 3).故意抛出一个异常
# 4).新增一条英雄人物数据（name:孙悟空 gender:1 book_id:4）

# 导包
import pymysql

try:
    # 获取数据库连接
    conn = pymysql.connect(host="8.131.250.56", user="root", passwd="passwordMYSQL123", database="books", port=3308,
                           autocommit=True)
    # 设置是否自动提交事务
    # conn.autocommit(False)

    # 获取游标对象
    cursor = conn.cursor()
    # 执行操作
    # 2).新增一条图书数据（id:4 title:西游记 pub_date:1986-01-01 ）
    sql = "insert into t_book(id,title,pub_date) values(4, '西游记', '1986-01-01')"
    cursor.execute(sql)

    # 3).故意抛出一个异常
    # raise Exception("故意抛出一个异常")

    # 4).新增一条英雄人物数据（name:孙悟空 gender:1 book_id:4）
    sql = "insert into t_hero(name,gender,book_id) values('孙悟空', 1, 4)"
    cursor.execute(sql)

    # 提交事务
    conn.commit()
except Exception as e:
    # 回滚事务
    conn.rollback()

    print("error:", e)
finally:
    print("关闭资源。。。。。")
    # 关闭游标对象
    if cursor:
        cursor.close()
    # 关闭数据库连接
    if conn:
        conn.close()
