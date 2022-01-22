#!/usr/bin/env python
# -*- coding:utf-8 -*-


def count_string(str, substring):
    # 统计子串在字符串中出现了几次
    print("「{}」在字符串中出现了{}次：".format(substring, str.count(substring)))


if __name__ == '__main__':
    str = "HELLO WORD"
    count_string(str, "WORD")
    print("*" * 100, "\n")
    count_string(str, "L")
