import logging

import requests
from Python09FutureloanApiTestcaseDemo import run_suite


class LoginApi:
    run_suite.init_log_config()

    def __init__(self):
        # 登录URL
        self.login_url = run_suite.BASE_URL + "/member/login"

    # 登录
    def login(self, mobile_phone, pwd):
        # data = {"mobile": mobile, "password": pwd}
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
            "Content-Type": "application/json",
            "X-Lemonban-Media-Type": "lemonban.v1"
        }
        logging.info("开始请求登录接口")
        return requests.post(self.login_url, json=ruquest_data, headers=header_data)


if __name__ == '__main__':
    res = LoginApi().login(13343608510, "1234567@")
    logging.info("main test res.json = {} \n".format(res.json()))
