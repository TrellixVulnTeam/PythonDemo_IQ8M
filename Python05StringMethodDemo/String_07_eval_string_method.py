#!/usr/bin/env python
# -*- coding:utf-8 -*-


if __name__ == '__main__':
    # # 将字符串内容进行基本数学计算
    num = eval("4*5")
    num01 = eval("4+5*2-6")
    print("解析字符串里的计算公式", num)
    print("解析字符串里的计算公式", num01)
    # 将字符串转换成列表
    list1 = eval("[1, 2, 3, 4, 5]")
    print("list1类型为：", type(list1))
    # 将字符串转换成字典
    dict1 = eval("{'name':'刘备','age':31,'sex':'男'}")
    print("dict1类型为：", type(dict1))
