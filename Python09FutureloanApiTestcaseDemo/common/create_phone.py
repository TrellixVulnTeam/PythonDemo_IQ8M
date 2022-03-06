#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @name: 生成手机号
# @Email:812011745@qq.com
# @Software:PyCharm
from loguru import logger
import random
import time


def create_a_phone():
    # 第二位数字
    second = [3, 5, 8][random.randint(0, 2)]

    # 第三位数字
    third = [2, 3, 5, 7, 8, 9][random.randint(0, 5)]

    # 最后八位数字
    suffix = str(int(time.time()))[2::]

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    for i in range(10):
        phone = create_a_phone()
        logger.info(phone)
        time.sleep(1)
