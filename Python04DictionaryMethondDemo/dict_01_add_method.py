#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 集合
def dict_add_method():
    # 定义一个字典
    set_data = {}
    return set_data


def get_all_data(data):
    num = 0
    for n in data:
        num += 1
        # n就是集合的所以键
        value = data.get(n)
        print("data第{}个数据为：{}:{}".format(num, n, value))

    print("_" * 100)
    print()


if __name__ == '__main__':
    data = dict_add_method()
    print("_" * 100)
    # 当前集合为空值
    print(*data)

    print(type(data))
    data["Name"] = "张飞"
    data["Age"] = 25
    data["height"] = 1.75

    # 如果这个键存在则更新值内容
    data["age"] = 20
    get_all_data(data)

    print(data)
