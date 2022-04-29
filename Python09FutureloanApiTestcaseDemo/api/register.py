import logging

from requests import request
from common import utils
from common import getPhoneNumber


class RegisterApi:
    # 注册
    @staticmethod
    def register(mobile_phone, pwd, type_int, reg_name="AutoTestPy"):
        # 注册URL
        login_url = utils.BASE_URL + "/member/register"
        ruquest_data = None
        if mobile_phone is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["mobile_phone"] = mobile_phone
        if pwd is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["pwd"] = pwd
        if type_int is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["type"] = type_int
        if reg_name is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["reg_name"] = reg_name

        logging.debug("request= {}".format(ruquest_data))
        logging.info("开始请求注册接口 ing ")
        return request('post', login_url, json=ruquest_data, headers=utils.header_data)


if __name__ == '__main__':
    # 拼接手机号
    phone = getPhoneNumber.getPhoneNumber()
    password = utils.BSAE_PASSWORD
    response = RegisterApi.register(phone, password, 1)
    logging.info("response= {} \n".format(response.json()))
