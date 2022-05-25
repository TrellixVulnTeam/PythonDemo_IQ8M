#!/usr/bin/env python
# -*- coding#utf-8 -*-
# @Time #2022/5/25 22:16
# @Author #夏见。
# @File #create_tmp_env_demo01.py

import os

"""
创建临时变量
"""

# 设置环境变量
os.environ['WORKON_HOME'] = "value"
# 获取环境变量方法1
tmp_env = os.environ.get('WORKON_HOME')
print(tmp_env)
# 获取环境变量方法2(推荐使用这个方法)
os.getenv('path')
# 删除环境变量
del os.environ['WORKON_HOME']

# # 设置常见环境变量
os.environ['http_proxy'] = "http://127.0.0.1/"  # 代理url(如127.0.0.1)

os.environ['HOMEPATH'] = "/root"  # 当前用户主目录
os.environ['TEMP'] = "/tmp"  # 临时目录路径
os.environ['PATHEXT']  # 可执行文件
os.environ['SYSTEMROOT']  # 系统主目录
os.environ['LOGONSERVER']  # 机器名
os.environ['PROMPT']  # 设置提示符
print(os.environ.get("http_proxy"))
