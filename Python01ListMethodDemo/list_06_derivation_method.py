#!/usr/bin/env python
# -*- coding:utf-8 -*-


if __name__ == '__main__':
    # 列表推导式 定义一个长列表
    # 从1到99步长为2的所以数字
    data = [x for x in range(1, 100, 2)]
    # 从1到99所以能被3整除的数字
    data1 = [x for x in range(1, 100, 2) if x % 3 == 0]
    # 解包list
    print(*data)
    print(*data1)
