import logging.handlers
import os
import time

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print("BASE_DIR=", BASE_DIR)

# 项目基本路径
BASE_URL = "http://api.mypeng.site/futureloan"
# 请求头数据
header_data = {
    "Content-Type": "application/json",
    "X-Lemonban-Media-Type": "lemonban.v1"
}


# 初始化日志配置
def init_log_config():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建处理器（控制台、文件处理器）
    sh = logging.StreamHandler()
    log_file = BASE_DIR + "/log/futureloan_{}.log".format(time.strftime('%Y_%m_%d_%H', time.localtime()))
    fh = logging.handlers.TimedRotatingFileHandler(log_file, when="midnight", interval=1,
                                                   backupCount=7, encoding="UTF-8")
    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 把格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)


if __name__ == '__main__':
    init_log_config()
    logging.info("test")
