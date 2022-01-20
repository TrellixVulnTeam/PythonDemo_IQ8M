#!/usr/bin/env python
# -*- coding:utf-8 -*-


if __name__ == '__main__':
    # 去除左边的空格
    left_str = "   左边有空格"
    print("去除左边的空格\t『" + left_str.lstrip() + "』")

    # 去除右边的空格
    right_str = "我的右边有空格   "
    print("去除我右边的空格\t『" + right_str.rstrip() + "』")

    # 去除左右两侧空格
    both_sides_str = "     我的2边都有空格   "
    print("去除2边的空格\t\t『" + both_sides_str.strip() + "』")
