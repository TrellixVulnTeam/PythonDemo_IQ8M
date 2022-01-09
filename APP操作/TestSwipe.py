# -*- coding: utf-8 -*-#


class Base_Page:
    def __init__(self, driver):
        self.driver = driver

    def width(self):
        """
        获取屏幕宽度
        :return:
        """
        return self.driver.get_window_size()['width']

    def height(self):
        """
        获取屏幕高度
        :return:
        """
        return self.driver.get_window_size()['height']

    def swipe_left(self):
        """
        向左滑动
        :return:
        """
        return self.driver.swipe(self.width() * 0.9, self.height() * 0.5, self.width() * 0.1, self.height() * 0.5)

    def swipe_right(self):
        """
        向右滑动
        :return:
        """
        return self.driver.swipe(self.width() * 0.9, self.height() * 0.5, self.width() * 0.1, self.height() * 0.5)

    def swipe_up(self):
        """
        向上滑动
        :return:
        """
        return self.driver.swipe(self.width() * 0.5, self.height() * 0.9, self.width() * 0.5, self.height() * 0.1)

    def swipe_down(self):
        """
        向下滑动
        :return:
        """
        return self.driver.swipe(self.width() * 0.5, self.height() * 0.1, self.width() * 0.5, self.height() * 0.9)

    def swipe(self, direction):
        """

        :param direction: 操作方法
        :return:
        Usage：swipe('left')
        """
        # 映射
        swipe_action = {
            'left': self.swipe_left,
            'right': self.swipe_right,
            'up': self.swipe_up,
            'down': self.swipe_down
        }
        # 判断是否有条件映射
        if direction not in swipe_action:
            raise ValueError('参数不正确')
        # 调用方法返回滑动操作
        return swipe_action[direction]()


if __name__ == '__main__':
    print(__name__)
