#!/usr/bin/env python
# -*- coding:utf-8 -*-


def list_add_method():
    list_date = []
    return list_date


# 遍历输出列表所以内容
def get_all_data(data):
    for n in data:
        print("list_data第", data.index(n), end="")
        print("个数据为：", n)
    print("_" * 100)
    print()


if __name__ == '__main__':
    data = list_add_method()
    data.append("append在末尾添加数据")
    get_all_data(data)

    data.insert(0, "insert在指定索引位置增加数据")
    get_all_data(data)

    list_extend_date = ["飞花", "血月"]
    # extend方法 追加另一个列表的值到这个列表
    data.extend(list_extend_date)
    get_all_data(data)
