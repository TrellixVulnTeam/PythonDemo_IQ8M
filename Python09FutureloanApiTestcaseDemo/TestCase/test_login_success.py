import unittest

from api.login import LoginApi
from common import utils
import logging
from parameterized import parameterized


class TestLoginSuccess(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    # 登录成功
    def test_login_success(self):
        # 测试数据
        mobile = "13800000002"
        pwd = "12345678"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("response={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")

        # 保存token数据
        token = json_data["data"]["token_info"]["token"]
        utils.header_data["Authorization"] = "Bearer " + token
        logging.info("utils.header_data=={}".format(str(utils.header_data)))
