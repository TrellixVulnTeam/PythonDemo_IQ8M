#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @name: 登录
# @Email:812011745@qq.com
# @Software:PyCharm

import time
import logging
import requests
from Python07RequestsDemo import reques_02_post_register


# 发送POST请求，请求体数据JSON格式
class PostDemo:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    def __init__(self):
        # 发送POST请求：提交表单数据
        self.heander_data = None
        self.login_data = None
        data = reques_02_post_register.PostDemo()
        data.post_register()  # 运行注册接口，获取新鲜的手机号密码登录
        base_url = "http://api.mypeng.site/futureloan"
        url_path = "/member/login"
        self.url = base_url + url_path
        self.phone = data.phone
        self.password = data.password

    def post_login(self):
        self.login_data = {
            "mobile_phone": self.phone,
            "pwd": self.password
        }
        self.heander_data = {
            "X-Lemonban-Media-Type": "lemonban.v1"
        }
        logging.info("开始运行登录接口")
        res = requests.post(self.url, headers=self.heander_data, json=self.login_data)
        logging.info("登录接口返回结果\n{}".format(res.json()))
        return res


if __name__ == '__main__':
    for n in range(10):
        print("*" * 100)
        # 获取响应结果
        res = PostDemo().post_login()
        # print("text=", res.text)
        # print("json=", res.json())
        # print(res.headers)
        # print(type(res.json()))
        # 输出code状态码和msg文案
        # print(res.json()["code"])
        # print(res.json()["msg"])
        # print("*" * 100)
        # time.sleep(1)
