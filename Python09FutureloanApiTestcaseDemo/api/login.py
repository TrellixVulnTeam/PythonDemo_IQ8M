#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 10:50 PM
# @Author : 夏见。
# @File : login.py

import logging

import requests

from common import utils


class LoginApi:

    def __init__(self):
        # 登录URL
        self.login_url = utils.BASE_URL + "/member/login"
        logging.info("login_url: {}".format(self.login_url))

    # 登录
    def login(self, mobile_phone, pwd):
        ruquest_data = None
        if mobile_phone is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["mobile_phone"] = mobile_phone
        if pwd is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["pwd"] = pwd

        header_data = {
            "X-Lemonban-Media-Type": "lemonban.v2"
        }
        logging.debug("开始请求登录接口ing")
        response = requests.post(self.login_url, json=ruquest_data, headers=header_data)
        logging.info(f"response= {response.json()}")
        return response


if __name__ == '__main__':
    res = LoginApi().login("15851136191", "1234567@")
    # logging.info("main test res.json = {} \n".format(res.json()))
