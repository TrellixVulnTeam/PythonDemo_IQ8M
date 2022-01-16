# coding:utf-8
import logging
import os
from logging.handlers import RotatingFileHandler  #
import colorlog  # 控制台日志输入颜色

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


class Log:
    def __init__(self, logname='Access_log'):
        self.logname = os.path.join("..\log", '%s' % logname)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
            log_colors=log_colors_config)  # 日志输出格式

    def console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.handlers.TimedRotatingFileHandler(self.logname, when='MIDNIGHT', interval=1, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()  # 关闭打开的文件

    def debug(self, message):
        self.console('debug', message)

    def info(self, message):
        self.console('info', message)

    def warning(self, message):
        self.console('warning', message)

    def error(self, message):
        self.console('error', message)


if __name__ == "__main__":
    log = Log()
    log.debug("DEBUG 测试01")  # 如果你需要在打印字段中设置
    log.info("测试1")  # 如果你需要在打印字段中设置
    log.warning("测试4")
    log.error("wawawa,baocuol")
    log.info("测试1")  # 如果你需要在打印字段中设置
    log.debug("测试2")  # 如果你需要在打印字段中设置
    # log.error("ERROR，测试3")

