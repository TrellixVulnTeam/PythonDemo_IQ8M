#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @name: 获取单个会员信息
# @Email:812011745@qq.com
# @Software:PyCharm

import time
import logging
import requests
from Python07RequestsDemo import reques_03_post_login

class PostDemo:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    def __init__(self):
        # 发送POST请求：提交表单数据
        self.heander_data = None
        self.login_data = None
        mobile_id = reques_03_post_login.PostDemo().post_login().json()["data"]["id"]
        base_url = "http://api.mypeng.site/futureloan"
        url_path = "/member/{}/info".format(mobile_id)
        self.url = base_url + url_path

    def get_info(self):
        self.heander_data = {
            "X-Lemonban-Media-Type": "lemonban.v1"
        }
        logging.info("开始获取用户信息接口")
        res = requests.get(self.url, headers=self.heander_data)
        logging.info("用户信息返回结果\n{}".format(res.json()))
        time.sleep(0.01)
        return res


if __name__ == '__main__':
    for n in range(5):
        print("*" * 100)
        # 获取响应结果
        res = PostDemo().get_info()
        # print("text=", res.text)
        # print("json=", res.json())
        # print(res.headers)
        # print(type(res.json()))
        # 输出code状态码和msg文案
        # print(res.json()["code"])
        # print(res.json()["msg"])
        # print("*" * 100)
        # time.sleep(1)
