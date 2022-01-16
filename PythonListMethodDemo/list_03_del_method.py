#!/usr/bin/env python
# -*- coding:utf-8 -*-


def list_del_method():
    list_date = ["采薇采薇，薇亦作止", "曰归曰归，岁亦莫止", "靡室靡家，猃狁之故", "不遑启居，猃狁之故"]
    return list_date


# 遍历输出列表所以内容
def get_all_data(data):
    for n in data:
        print("list_data第", data.index(n), end="")
        print("个数据为：", n)
    print("_" * 100)
    print()


if __name__ == '__main__':
    data = list_del_method()
    get_all_data(data)

    del (data[0])  # 删除指定索引的数据
    get_all_data(data)

    data.pop(1)  # 删除指定索引数据
    get_all_data(data)

    data.pop()  # 删除末尾数据
    get_all_data(data)

    data.clear()  # 清空列表
    get_all_data(data)
