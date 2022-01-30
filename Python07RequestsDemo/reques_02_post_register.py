#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @name: 注册
# @Email:812011745@qq.com
# @Software:PyCharm

# 请求TPshop项目的登录接口，请求数据（username: 13088888888, password: 123456, verify_code: 1234）
# 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login

# 导包
import logging
import time

import requests
import create_phone


class PostDemo:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    def __init__(self):
        # 发送POST请求：提交表单数据
        self.register_data = None
        base_url = "http://api.mypeng.site/futureloan"
        url_path = "/member/register"
        self.url = base_url + url_path
        self.phone = create_phone.create_a_phone()
        # print(self.phone)
        self.password = "1234567@"

    def post_register(self):
        self.register_data = {
            "mobile_phone": self.phone,
            "pwd": self.password,
            "type": 1,
            "reg_name": "{}".format(int(time.time()))

        }
        self.heander_data = {
            "X-Lemonban-Media-Type": "lemonban.v1"
        }
        logging.info("运行注册接口")
        res = requests.post(self.url, headers=self.heander_data, json=self.register_data)
        logging.info("注册接口返回结果：\n{}".format(res.json()))
        return res


if __name__ == '__main__':
    for n in range(1):
        # 获取响应结果
        res = PostDemo().post_register()
        # print("text=", res.text)
        # print("json=", res.json())
        # print(res.headers)
        # print(type(res.json()))
        # 输出code状态码和msg文案
        # print(res.json()["code"])
        # print(res.json()["msg"])
        # print("*" * 100)
        # time.sleep(1)
