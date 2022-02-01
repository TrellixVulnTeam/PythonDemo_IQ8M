import logging
import random
import time

from requests import request

from Python09FutureloanApiTestcaseDemo import run_suite
from Python09FutureloanApiTestcaseDemo.common import create_phone

run_suite.init_log_config()


# 注册
def login(mobile_phone, pwd, type_int, **kwargs):
    # 注册URL
    login_url = run_suite.BASE_URL + "/member/register"
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
    res = login(phone, "1234567@", 1)
    logging.info("main test res.json = {} \n".format(res.json()))
