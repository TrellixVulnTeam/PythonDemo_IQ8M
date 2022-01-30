#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @Email:812011745@qq.com
# @Software:PyCharm

# 请求url
import requests as requests

url = "http://httpbin.org/get"
# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "python-requests/2.9.1"}
# 查询字符串
params = {'name': 'coco', 'age': '18'}
res = requests.get(url, headers=headers, data=params)

# 获取响应状态码 res.status_code
print("响应状态码:", res.status_code)

# 获取响应消息 res.content
print("响应消息:", res.content)

# 获取请求头 res.request.headers
print("请求头:", res.request.headers)

# 获取响应头 res.headers
print("响应头:", res.headers)

# 获取响应数据 res.text
print("响应数据:", res.text)

# 获取cookie res.cookies
print("cookie:", res.cookies)

# res.json（）
print("json:", res.json())
