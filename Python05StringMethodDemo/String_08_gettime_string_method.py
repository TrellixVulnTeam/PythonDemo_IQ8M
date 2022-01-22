#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

if __name__ == '__main__':
    strtime = time.strftime("%Y.%m.%d %H:%M:%S")
    # 打印当前时间
    print(strtime)

    """
    %Y  Year with century as a decimal number. 年
    %m  Month as a decimal number [01,12]. 月
    %d  Day of the month as a decimal number [01,31]. 日
    %H  Hour (24-hour clock) as a decimal number [00,23]. 时
    %M  Minute as a decimal number [00,59]. 分
    %S  Second as a decimal number [00,61]. 秒
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
    """
