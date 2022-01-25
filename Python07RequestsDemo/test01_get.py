#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @Email:812011745@qq.com
# @Software:PyCharm

import requests

# 发送GET请求
response = requests.get("http://www.baidu.com")

# 获取响应数据
print(response.text)
