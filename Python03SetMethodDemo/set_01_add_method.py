#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 集合是无序的，不存在下标的概念
def set_add_method():
    # 创建空集合不能使用 data={} 需使用以下方法定义空集合
    set_data = set()
    return set_data


if __name__ == '__main__':
    data = set_add_method()
    print("_" * 100)
    # 当前集合为空值
    print(*data)
    print("_" * 100)

    print(type(data))
    data.add("Add")
    data.add("Test")
    data.add("Hello word")
    data.add(1101)
    print(*data)
    print("_" * 100)
