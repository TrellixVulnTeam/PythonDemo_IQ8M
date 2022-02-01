import time

# print(time.time())


# print(time.strftime('%Y-%m-%d', time.localtime()))
# print(time.strftime('%Y年%m月%d日 %H时%M分%S秒', time.localtime()))

class GetTime:
    def get_now_time(self):
        print(time.strftime('%H:%M:%S', time.localtime()))

    def return_timeout(self):
        time_out = time.strftime('%Y_%m_%d_%H', time.localtime())
        print(time_out)
        return time_out


if __name__ == '__main__':
    GetTime().get_now_time()
    GetTime().return_timeout()
