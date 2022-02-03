import random
import time
import unittest
import logging

from Python09FutureloanApiTestcaseDemo.api.register import Register_Api
from Python09FutureloanApiTestcaseDemo.common import utils
import json
from parameterized import parameterized


# [(), (), ()]
def build_data():
    test_data = []
    with open(utils.BASE_DIR + "/data/register.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            # mobile_phone = case_data.get("mobile_phone")
            mobile_phone = "1{}{}{}".format([3, 5, 8][random.randint(0, 2)], [2, 3, 5, 7, 8, 9][random.randint(0, 5)],
                                            str(int(time.time()))[2::])
            pwd = case_data.get("pwd")
            type_int = case_data.get("type_int")
            reg_name = case_data.get("reg_name")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((mobile_phone, pwd, type_int, reg_name, status_code, code, msg))
        logging.info("test_data={}".format(test_data))
    return test_data


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.register_api = Register_Api

    @parameterized.expand(build_data)
    def test_login(self, mobile_phone, pwd, type_int, reg_name, status_code, code, msg):
        # 登录
        response = self.register_api.register(mobile_phone, pwd, type_int, reg_name, )
        json_data = response.json()
        logging.info("json_data={}\n".format(json_data))
        # 断言
        utils.common_assert(self, response, status_code, code, msg)

    @unittest.skip
    def test_register_success(self):
        # 测试数据
        mobile = "1{}{}{}".format([3, 5, 8][random.randint(0, 2)], [2, 3, 5, 7, 8, 9][random.randint(0, 5)],
                                  str(int(time.time()))[2::])
        pwd = "1234567@"
        type_int_int = 1

        # 登录
        response = self.register_api.register(mobile, pwd, type_int_int)
        json_data = response.json()
        # print(json_data)
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")
