import unittest
from Python09FutureloanApiTestcaseDemo.common import utils

from Python09FutureloanApiTestcaseDemo.TestCase.test_login01 import TestLogin
from Python09FutureloanApiTestcaseDemo.tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(Tregister))

unittest.TextTestRunner().run(suite)
# print("")

# report_file = utils.BASE_DIR + "/report/report.html"
# with open(report_file, "wb") as f:
#     runner = HTMLTestRunner(f, title="ihrm接口测试报告", description="xxx")
#     runner.run(suite)
