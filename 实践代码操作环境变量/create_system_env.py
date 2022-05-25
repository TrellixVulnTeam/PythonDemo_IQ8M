#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/25 22:23
# @Author : 夏见。
# @File : create_system_env.py

import os
import sys

path = r"E:\TMP\env"
command = r"setx work %s /m" % path  # / m代表系统变量。
# command = r"setx work %s" % path  # 不加 / m为用户变量
os.system(command)

# 遍历环境变量
env_list = os.environ
for key in env_list:
    print(key + ":" + env_list[key])
