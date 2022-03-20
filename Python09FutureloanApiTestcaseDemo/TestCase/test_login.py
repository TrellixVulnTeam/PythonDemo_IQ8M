import unittest
from loguru import logger

from Python09FutureloanApiTestcaseDemo.api.login import LoginApi
from Python09FutureloanApiTestcaseDemo.common import utils

from parameterized import parameterized


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    # 登录成功

    def test_login_success(self):
        # 测试数据
        mobile = "13216365136"
        pwd = "12345678"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logger.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 0)

        # 保存token数据
        token = json_data["data"]["token_info"]["token"]
        utils.header_data["Authorization"] = "Bearer " + token
        logger.info("utils.header_data=\n"+str(utils.header_data))
