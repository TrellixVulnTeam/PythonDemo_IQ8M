import unittest
import logging

from api.login import LoginApi
from common import utils
import json
from parameterized import parameterized

from common.utils import init_log_config


# 构造测试数据，读取JSON文件
# [(), (), ()]
def build_data():
    test_data = []
    with open(utils.BASE_DIR + "/data/login.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            mobile_phone = case_data.get("mobile_phone")
            pwd = case_data.get("pwd")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((mobile_phone, pwd, status_code, code, msg))
        # print(test_data)
        logging.info(" Test_data={}".format(test_data))
    return test_data


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        init_log_config()
        cls.login_api = LoginApi()

    # 登录
    @parameterized.expand(build_data)
    def test_login(self, mobile_phone, pwd, status_code, datacode, msg):
        print("执行了这个方法 test_login")
        logging.info("打印参数 {}，{}，{}，{}，{}".format(mobile_phone, pwd, status_code, datacode, msg))
        # 登录
        res = self.login_api.login(mobile_phone, pwd)
        json_data = res.json()
        logging.info("json_data :={}".format(json_data))
        # 断言
        # utils.common_assert(self, response, status_code)
        # print("*** " * 10)
        # print(json_data["code"])
        # print("*** " * 10)
        self.assertEqual(json_data["code"], datacode, "断言返回消息体的code码")
        self.assertEqual(json_data["msg"], msg, "断言msg消息")
        logging.info("断言结束，用例执行结束")
        # 保存token数据
        # if success:
        #     token = json_data.get("data")
        #     utils.header_data["Authorization"] = "Bearer " + token
        #     print("app.header_data==", utils.header_data)
        #     # app.a = 2

    # 登录成功
    # @unittest.skip
    def test_login_success(self):
        # 测试数据
        mobile = "13800000002"
        pwd = "12345678"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")

        # print("保存token之前的hraders==", utils.header_data)
        # 保存token数据
        token_type = json_data.get("data").get("token_info").get("token_type")
        token = json_data.get("data").get("token_info").get("token")
        # print("打印登录后获取到的token", token_type)
        utils.header_data["Authorization"] = token_type + " " + token
        print("app.header_data==", utils.header_data)
        # app.a = 2

    # 用户名不存在
    @unittest.skip
    def test_username_is_not_exist(self):
        # 测试数据
        mobile = "13888889969"
        pwd = "123456"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 104, "1004")

        # self.assertEqual(200, response.status_code)
        # self.assertEqual(False, json_data.get("success"))
        # self.assertFalse(json_data.get("success"))
        # self.assertEqual(20001, json_data.get("code"))
        # self.assertIn("用户名或密码错误", json_data.get("message"))

    # 密码错误
    @unittest.skip
    def test_pwd_is_error(self):
        # 测试数据
        mobile = "13800000002"
        pwd = "error"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 20001, "用户名或密码错误")

    # 请求参数为空
    # @unittest.skip
    def test_req_param_is_null(self):
        # 测试数据
        mobile = None
        pwd = None

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 1004, "密码为空")
