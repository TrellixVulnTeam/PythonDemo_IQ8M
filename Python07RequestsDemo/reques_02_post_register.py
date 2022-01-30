#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @name: 注册
# @Email:812011745@qq.com
# @Software:PyCharm

# 请求TPshop项目的登录接口，请求数据（username: 13088888888, password: 123456, verify_code: 1234）
# 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login

# 导包
import time

import requests
import create_phone


class PostDemo:
    def __init__(self):
        # 发送POST请求：提交表单数据
        self.login_data = None
        base_url = "http://api.mypeng.site/futureloan"
        url_path = "/member/register"
        self.url = base_url + url_path
        self.phone = create_phone.create_a_phone()
        print(self.phone)
        self.password = "1234567@"

    def post_register(self):
        self.login_data = {
            "mobile_phone": self.phone,
            "pwd": self.password,
            "type": 1,
            "reg_name": "{}".format(int(time.time()))

        }
        self.heander_data = {
            "X-Lemonban-Media-Type": "lemonban.v1"
        }

        return requests.post(self.url, headers=self.heander_data, json=self.login_data)


if __name__ == '__main__':
    for n in range(10):
        # 获取响应结果
        res = PostDemo().post_register()
        # print("text=", res.text)
        print("json=", res.json())
        # print(res.headers)
        # print(type(res.json()))
        # 输出code状态码和msg文案
        print(res.json()["code"])
        print(res.json()["msg"])
        print("*" * 100)
        time.sleep(1)
