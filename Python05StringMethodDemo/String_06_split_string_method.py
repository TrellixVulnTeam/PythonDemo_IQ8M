#!/usr/bin/env python
# -*- coding:utf-8 -*-


def split_string(str, symbol):
    # 拆分字符串
    print("根据逗号拆分字符串,原值{}，原值类型{}".format(str, type(str)))
    list = str.split(symbol)
    print("拆分后数据类型为：{}".format(type(list)))
    print("拆分后数据为：{}".format(list))
    return list

if __name__ == '__main__':
    str = "HelloWord,HellePython"
    split_string(str, ",")
    print("*" * 100, "\n")
    str = "1 2 3 4 5 6 67 1"
    list = split_string(str, " ")
    # for n in list:
    #     print(n)
