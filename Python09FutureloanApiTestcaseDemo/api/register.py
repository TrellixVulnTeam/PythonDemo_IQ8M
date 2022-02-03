import logging
import random
import time

from requests import request
from Python09FutureloanApiTestcaseDemo.common import utils
from Python09FutureloanApiTestcaseDemo import api


# 注册
def register(mobile_phone, pwd, type_int, reg_name="Auto_Test"):
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

    header_data = {
        "Content-Type": "application/json",
        "X-Lemonban-Media-Type": "lemonban.v1"
    }
    logging.info("requesdate = {}".format(ruquest_data))
    logging.info("开始请求注册接口")
    return request('post', login_url, json=ruquest_data, headers=header_data)


if __name__ == '__main__':
    # 拼接手机号
    phone = "1{}{}{}".format([3, 5, 8][random.randint(0, 2)], [2, 3, 5, 7, 8, 9][random.randint(0, 5)],
                             str(int(time.time()))[2::])
    res = register(phone, "1234567@", 1)
    # res = register(phone, "1234567@", 1, 123)
    logging.info("main test res.json = {} \n".format(res.json()))
