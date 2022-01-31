#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:xiajian
# @name: 体现
# @Email:812011745@qq.com
# @Software:PyCharm

import time
import logging
import requests
from Python07RequestsDemo import reques_03_post_login
from Python07RequestsDemo import reques_04_post_recharge


# 发送POST请求，请求体数据JSON格式
class PostDemo:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    def __init__(self):
        # 获取到ID，准备充值
        try:
            member_id = reques_04_post_recharge.PostDemo().post_recharge().json()["data"]["id"]
            self.withdraw_data = {
                "member_id": member_id,
                "amount": 6000
            }
            logging.info("获取到member_id：{}".format(member_id))
            base_url = "http://api.mypeng.site/futureloan"
            url_path = "/member/withdraw"
            self.url = base_url + url_path

        except:
            logging.error("手机号不存在，换个手机号试试")
            self.url = None
            return

    def post_withdraw(self):
        # print(self.url)
        if self.url is None:
            return
        else:
            self.heander_data = {
                "Content-Type": "application/json",
                "X-Lemonban-Media-Type": "lemonban.v1"
            }
            logging.info("开始运行提现接口")
            print(self.withdraw_data)
            res = requests.post(self.url, headers=self.heander_data, json=self.withdraw_data)
            logging.info("提现接口返回结果\n{}".format(res.json()))
            return res


if __name__ == '__main__':
    for n in range(1):
        print("*" * 100)  # 唯一分隔符
        # 获取响应结果
        res = PostDemo().post_withdraw()
        # print("text=", res.text)
        # print("json=", res.json())
        # print(res.headers)
        # print(type(res.json()))
        # 输出code
        # 状态码和msg文案
        if res is None:
            continue
    else:
        logging.info("响应码：{}".format(res.json()["code"]))
        # print(res.json()["msg"])
        # print("*" * 100)
        # time.sleep(1)
