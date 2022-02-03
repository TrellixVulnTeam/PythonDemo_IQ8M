import logging
import requests
from Python09FutureloanApiTestcaseDemo.common import utils
from Python09FutureloanApiTestcaseDemo import api


class LoginApi:

    def __init__(self):
        # 登录URL
        self.login_url = utils.BASE_URL + "/member/login"

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

        logging.info("开始请求登录接口")
        return requests.post(self.login_url, json=ruquest_data, headers=utils.header_data)


if __name__ == '__main__':
    res = LoginApi().login(13343608510, "1234567@")
    logging.info("main test res.json = {} \n".format(res.json()))
