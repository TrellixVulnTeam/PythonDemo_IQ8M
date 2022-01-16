#!/usr/bin/env python
# -*- coding:utf-8 -*-


def list_update_method():
    list_date = ["诗句如画", "岂不美哉"]
    return list_date


# 遍历输出列表所以内容
def get_all_data(data):
    for n in data:
        print("list_data第", data.index(n), end="")
        print("个数据为：", n)
    print("_" * 100)
    print()


if __name__ == '__main__':
    data = list_update_method()
    data.append("append在末尾添加数据")
    get_all_data(data)

    data[1] = "修改index为1的数据为NONE"
    get_all_data(data)
