# 数据操作的工具类
# 实现的功能：
# 获取数据库连接对象
# 关闭数据库连接对象
# 获取游标对象
# 关闭游标对象
# 查询一条记录

import pymysql


class DBUtil:
    __conn = None

    # 获取数据库连接对象
    @classmethod
    def get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="api.mypeng.site", user="root", passwd="Lemon123456!", database="books",
                                         port=3305)
        return cls.__conn

    # 关闭数据库连接对象
    @classmethod
    def close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None

    # 获取游标对象
    @classmethod
    def get_cursor(cls):
        # return cls.__conn.cursor()
        return cls.get_conn().cursor()

    # 关闭游标对象
    @classmethod
    def close_cursor(cls, cursor):
        if cursor:
            cursor.close()

    # 查询一条记录
    @classmethod
    def get_one(cls, sql):
        cursor = DBUtil.get_cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        DBUtil.close_cursor(cursor)
        DBUtil.close_conn()
        return result


if __name__ == '__main__':
    result = DBUtil.get_one("select * from t_book where id=1")
    print("result==", result)
