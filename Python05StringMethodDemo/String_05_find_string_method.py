#!/usr/bin/env python
# -*- coding:utf-8 -*-


def find_string(str, findstr):
    # 查找字符串中指定的子串
    print("查找带{}的字符串位置，不存在返回-1，结果：".format(findstr), str.find(findstr))


def replace_string(str, data, repl):
    # 查找替换
    newstr = str.replace(data, repl)
    print("输出一个新的字符串", newstr)


if __name__ == '__main__':
    data = ["你好", "HELLO WORD"]
    for n in data:
        print("字符串的长度为：", len(n))
        # 查找带H子串的str并返回下标，不存在返回-1
        find_string(n, "WORD")
        # 查找WORD替换为Python，找不到既不修改直接赋值
        replace_string(n, "WORD", "PYTHON")
        print("*" * 100, "\n")
