#!/usr/bin/env python
# -*- coding:utf-8 -*-


if __name__ == '__main__':
    str = "hello word"
    # # 1字母处理：
    # .upper()    # 全部大写
    print("全部大写\t\t", str.upper())
    # 输出结果 全部大写		 HELLO WORD
    # .lower()    # 全部小写
    print("全部小写\t\t", str.lower())
    # 输出结果 全部小写		 hello word
    # .swapcase()    # 大小写互换
    print("大小写互换\t", str.swapcase())
    # 输出结果 大小写互换	 HELLO WORD
    strnow = "The first letter is uppercase and the rest is lowercase.Good night"
    # .capitalize()    # 首字母大写，其余小写
    print("首字母大写，其余小写\t", strnow.capitalize())
    # 输出结果  首字母大写，其余小写	 The first letter is uppercase and the rest is lowercase.good night
    # .title()    # 首字母大写
    print("首字母大写\t", str.title())
    # 输出结果  首字母大写	 Hello Word
