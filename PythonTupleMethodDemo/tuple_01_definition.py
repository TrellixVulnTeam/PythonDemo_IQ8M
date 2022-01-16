#!/usr/bin/env python
# -*- coding:utf-8 -*-


if __name__ == '__main__':
    # 元祖和列表区别式，元祖定义后不可修改
    # 定义一个空元祖
    tuple01 = ()

    # 定义1个值得元祖，需要在值后面加，
    str = ("Test")
    tuple02 = ("Test",)
    print("str的类型为：", type(str))
    print("tuple02的类型为：", type(tuple02))

    # 定义元祖可省略括号
    tuple03 = "Test", "我是元祖", "Test"

    print("tuple03的类型为：", type(tuple03))
    print(*tuple03)

    for n in tuple03:
        print(tuple03.index(n))
        print(tuple03.count(n))
