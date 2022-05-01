#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/1 12:12 PM
# @Author : 夏见。
# @File : get_env.py

# 当前文件路径
import configparser
import os

proDir = os.path.dirname(os.path.dirname(__file__)) + "/env"

# print(proDir)
# 在当前文件路径下查找.ini文件
#
configPath = os.path.join(proDir, "test.ini")

print(configPath)
conf = configparser.ConfigParser()

# 读取.ini文件

conf.read(configPath)

# get()函数读取section里的参数值

name = conf.get("section1", "name")
print(name)
#
print(conf.sections())  # 获取所有的标题

print(conf.options('section1'))  # 获取键

print(conf.items('section1'))  # 获取键值对
