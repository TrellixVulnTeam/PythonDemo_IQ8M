#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

if __name__ == '__main__':
    str = "走天涯月亮依旧停在旷野上,你的身影被越拉越长,直到远去的马蹄声响,呼唤你的歌声传四方"

    print(str)
    # 字符串切片
    print("输出从第3个到第8个的字符串:  ", end="")
    print(str[2:9])
    print("输出第1到9的字符串，步长为2:  ", end="")
    print(str[0:10:2])

    print("截取最后2个字符:  ", end="")
    # 第二个值不填默认就是取到最后一位
    print(str[-2:])
    print("倒序输出一遍:  ", end="")
    print(str[::-1])
