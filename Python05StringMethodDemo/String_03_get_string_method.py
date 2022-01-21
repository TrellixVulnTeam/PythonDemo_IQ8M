#!/usr/bin/env python
# -*- coding:utf-8 -*-


def judgment_string(str):
    if str.isalpha():
        print("判断字符串是否为文字构成,仅支持纯文本")
    elif str.isdigit():
        print("判断字符串是否为数字构成,仅支持纯数字")
    elif str.islower():
        print("判断字符串中所有字母是否都为小写")
    elif str.isupper():
        print("判断字符串中所有字母是否都为大写")


def find_string(str):
    print("查找带{}的字符串位置，不存在返回-1，结果：".format("H"), str.find("H"))


if __name__ == '__main__':
    data = ["你好", "123", "hello word", "HELLO WORD"]
    for n in data:
        judgment_string(str(n))
        print("字符串的长度为：", len(n))
        find_string(n)
        # 获取字符串最后一位，字符串[索引] 得到指定索引位置的字符，字符串长度减一正好是最后一位，原因是：len从1计数，下标从0开始计数
        print(n[len(n) - 1])
        print("*" * 100, "\n")
