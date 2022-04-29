import random
import time
import unittest
import logging

from api.register import RegisterApi
from common import utils
from common import getPhoneNumber
import json
from parameterized import parameterized


class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.register_api = RegisterApi

    def test_register_success(self):
        # 测试数据
        mobile = getPhoneNumber.getPhoneNumber()
        pwd = "1234567@"
        type_int = 1

        # 注册
        response = self.register_api.register(mobile, pwd, type_int)
        json_data = response.json()
        print(json_data)
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")
