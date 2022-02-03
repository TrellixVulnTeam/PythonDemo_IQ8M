# import logging
# import random
# import time
#
# from Python09FutureloanApiTestcaseDemo.api import *
#
# # 拼接手机号
# phone = "1{}{}{}".format([3, 5, 8][random.randint(0, 2)], [2, 3, 5, 7, 8, 9][random.randint(0, 5)],
#                          str(int(time.time()))[2::])
# res = register(phone, "1234567@", 1)
# logging.info("main test res.json = {} \n".format(res.json()))
