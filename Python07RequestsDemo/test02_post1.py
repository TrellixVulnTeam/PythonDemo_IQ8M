#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @Email:812011745@qq.com
# @Software:PyCharm

# 请求TPshop项目的登录接口，请求数据（username: 13088888888, password: 123456, verify_code: 1234）
# 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login

# 导包
import requests

# 发送POST请求：提交表单数据
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "13088888888",
    "password": "123456",
    "verify_code": "1234",
}
response = requests.post(url, data=login_data)

# 获取响应结果
print("text=", response.text)
print("json=", response.json())
