import random
import time
import unittest
import logging

from Python09FutureloanApiTestcaseDemo.api import register
from Python09FutureloanApiTestcaseDemo.common import utils
import json
from parameterized import parameterized


class TestLogin(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.register_api = register

    # 登录成功

    def test_register_success(self):
        # 测试数据
        mobile = "1{}{}{}".format([3, 5, 8][random.randint(0, 2)], [2, 3, 5, 7, 8, 9][random.randint(0, 5)],
                                  str(int(time.time()))[2::])
        pwd = "1234567@"
        type_int = 1

        # 登录
        response = register.register(mobile, pwd, type_int)
        json_data = response.json()
        # print(json_data)
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")
