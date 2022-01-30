#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @name: 充值
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
        # 注册一个号，获取到ID，准备充值
        member_id = reques_02_post_register.PostDemo().post_register().json()["data"]["id"]
        self.recharge_data = {
            "member_id": member_id,
            "amount": 6300
        }
        logging.info("获取到member_id：{}".format(member_id))
        base_url = "http://api.mypeng.site/futureloan"
        url_path = "/member/recharge"
        self.url = base_url + url_path

    def post_recharge(self):
        self.heander_data = {
            "X-Lemonban-Media-Type": "lemonban.v1"
        }
        logging.info("开始运行充值接口")
        res = requests.post(self.url, headers=self.heander_data, json=self.recharge_data)
        logging.info("充值接口返回结果\n{}".format(res.json()))
        return res


if __name__ == '__main__':
    for n in range(100):
        print("*" * 100)  # 唯一分隔符
        # 获取响应结果
        res = PostDemo().post_recharge()
        # print("text=", res.text)
        # print("json=", res.json())
        # print(res.headers)
        # print(type(res.json()))
        # 输出code状态码和msg文案
        # print(res.json()["code"])
        # print(res.json()["msg"])
        # print("*" * 100)
        time.sleep(1)
