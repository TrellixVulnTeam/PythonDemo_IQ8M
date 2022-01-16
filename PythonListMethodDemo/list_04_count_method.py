#!/usr/bin/env python
# -*- coding:utf-8 -*-


def list_del_method():
    list_date = [5, 5, 4, 1, 7, 4, 5, 1, 6, 8, 8, 6, 6]
    return list_date


# 遍历输出列表所以内容
def get_all_data(data):
    for n in data:
        # 列表index函数，获取当前下标的值
        print("list_data第", data.index(n), end="")
        print("个数据为：", n)
    print("_" * 100)
    print()


if __name__ == '__main__':
    data = list_del_method()
    print("_" * 100)

    # 打印6在列表中出现了几次
    print("6在列表中出现了", data.count(6), "次")
    print("_" * 100)

    print("升序排序")
    data.sort()  # 升序排序
    get_all_data(data)

    print("降序排序")
    data.sort(reverse=True)  # 降序排序
    get_all_data(data)

    print("逆置，反转")
    data.reverse()
    get_all_data(data)
