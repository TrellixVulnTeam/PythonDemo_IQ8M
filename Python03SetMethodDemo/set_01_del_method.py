#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 集合是无序的，不存在下标的概念
def set_del_method():
    # 创建空集合不能使用 data={} 需使用以下方法定义空集合
    set_data = set()
    return set_data


def get_all_data(data):
    num = 0
    for n in data:
        num += 1
        print("data第{}个数据为：{}".format(num, n))
    print("_" * 100)
    print()


if __name__ == '__main__':
    data = set_del_method()
    print("_" * 100)
    data.add("用我三生烟火,换你一世迷离")
    data.add("我自是年少,韶华倾负。")
    data.add("Hello word")
    data.add("终是谁使弦断,花落肩头,恍惚迷离")
    get_all_data(data)

    msg = "删除指定的值,删除后结果为："
    print(msg)
    data.remove("Hello word")
    get_all_data(data)

    # 删除末尾的值
    print("删除末尾的值，但因为集合无序，所以删除的字段无法把控")
    data.pop()
    get_all_data(data)
