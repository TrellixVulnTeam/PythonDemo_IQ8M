#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/30 11:59 PM
# @Author : 夏见。
# @File : information.py
import logging

import requests

import login
from common import utils


class InForMation:

    def __init__(self, mobile_phone, pwd):
        # 请求登录接口获取member_id
        response = login.LoginApi().login(mobile_phone, pwd)
        member_id = response.json()["data"]["id"]
        print(member_id)
        self.info_url = utils.BASE_URL + "/member/{}/info".format(member_id)
        logging.info(f"info_url: {self.info_url}")
        # 保存token数据
        token = response.json()["data"]["token_info"]["token"]
        utils.header_data["Authorization"] = "Bearer " + token
        logging.info(f"utils.header_data== {utils.header_data}")

    # 获取个人信息
    def get_information(self):
        header_data = utils.header_data
        logging.debug("开始请求获取个人信息接口ing")
        response = requests.get(self.info_url, headers=header_data)
        logging.info(f"response= {response.json()}")
        return response


if __name__ == '__main__':
    from common.utils import init_log_config

    init_log_config()
    InForMation("15851136191", "1234567@").get_information()
