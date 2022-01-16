#!/usr/bin/env python
# -*- coding:utf-8 -*-


if __name__ == '__main__':
    # 元祖和列表区别式，元祖定义后不可修改
    # 定义一个空元祖
    tuple01 = ("Test", "我是元祖", "Test")

    print(type(tuple01))
    list01 = list(tuple01)
    print(type(list01))
    list01.append("转list后可修改数据")
    # 在转回tuple
    tuple02 = tuple(list01)
    print(type(tuple02))
    print(*tuple02)
