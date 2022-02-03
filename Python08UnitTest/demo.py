import time


class TimeTest:

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())


print(TimeTest.showTime())

# # t = TimeTest(2, 10, 10)
# nowTime = t.showTime()
# print(nowTime)
