import unittest


class TestLogin(unittest.TestCase):

    def test01_login_success(self):
        # 登录成功
        print("登录成功")

    def test02_login_not_phone(self):
        # 手机号不存在
        print("登录失败")
