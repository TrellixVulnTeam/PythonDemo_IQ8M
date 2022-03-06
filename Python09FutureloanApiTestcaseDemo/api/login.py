from loguru import logger
import requests
from Python09FutureloanApiTestcaseDemo.common import utils


class LoginApi:

    def __init__(self):
        # 登录URL
        self.login_url = utils.BASE_URL + "/member/login"
        logger.info("login_url:", self.login_url)

    # 登录
    def login(self, mobile_phone, pwd):
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
            "X-Lemonban-Media-Type": "lemonban.v1"
        }

        logger.info("开始请求登录接口")
        res = requests.post(self.login_url, json=ruquest_data, headers=header_data)
        logger.info(res.json())
        return res


if __name__ == '__main__':
    res = LoginApi().login("13826601726", "1234567@")
    # logging.info("main test res.json = {} \n".format(res.json()))
