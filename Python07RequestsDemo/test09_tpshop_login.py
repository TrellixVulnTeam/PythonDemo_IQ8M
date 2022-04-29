# 导包
import unittest

import requests


# 创建测试类
class TestTPshopLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.Session()
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self) -> None:
        self.session.close()

    # 创建测试方法
    # 登录成功
    def test01_login_success(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        # 断言
        self.assertEqual(200, response.status_code)
        content_type = response.headers.get("Content-Type")
        print("content_type=", content_type)
        self.assertIn("image", content_type)

        # 登录
        login_data = {
            "username": "13012345678",
            "password": "123456",
            "verify_code": "8888",
        }
        response = self.session.post(self.login_url, data=login_data)
        json_data = response.json()
        print("json_data==", json_data)

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, json_data.get("status"))
        self.assertIn("登陆成功", json_data.get("msg"))

    # 账号不存在
    def test02_username_is_not_exist(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        # 断言
        self.assertEqual(200, response.status_code)
        content_type = response.headers.get("Content-Type")
        print("content_type=", content_type)
        self.assertIn("image", content_type)

        # 登录
        login_data = {
            "username": "13088888888",
            "password": "123456",
            "verify_code": "8888",
        }
        response = self.session.post(self.login_url, data=login_data)
        json_data = response.json()
        print("json_data==", json_data)

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, json_data.get("status"))
        self.assertIn("账号不存在", json_data.get("msg"))

    # 密码错误
    def test03_pwd_is_error(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        # 断言
        self.assertEqual(200, response.status_code)
        content_type = response.headers.get("Content-Type")
        print("content_type=", content_type)
        self.assertIn("image", content_type)

        # 登录
        login_data = {
            "username": "13012345678",
            "password": "error",
            "verify_code": "8888",
        }
        response = self.session.post(self.login_url, data=login_data)
        json_data = response.json()
        print("json_data==", json_data)

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, json_data.get("status"))
        self.assertIn("密码错误", json_data.get("msg"))
