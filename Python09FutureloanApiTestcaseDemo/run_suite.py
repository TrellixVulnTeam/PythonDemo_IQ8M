import time
import unittest

from TestCase.test_login import TestLogin
from common import utils
from TestCase.test_login_success import TestLoginSuccess
from TestCase.test_register import TestRegister
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestLoginSuccess))
suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestRegister))

# unittest.TextTestRunner().run(suite)

report_file = utils.BASE_DIR + "/report/report{}.html".format(time.strftime('%Y_%m_%d_%H', time.localtime()))
# print(report_file)

with open(report_file, "w") as f:
    runner = HTMLTestRunner(f, title="API接口测试报告", description="xxx")
    runner.run(suite)
