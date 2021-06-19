# -*- coding: utf-8 -*-#

from appium import webdriver
import time
desired_caps = {
               "platformName": "Android",
               "platformVersion": "5.1",
               "deviceName": "U4KF9HSK99999999",
               "appPackage": "com.taobao.taobao",
               "appActivity": "com.taobao.tao.welcome.Welcome",
               "unicodeKeyboard":True,
               "resetKeyboard":True,
               "noReset": True
                }
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

def get_size():
    #获取窗口尺寸
    size=driver.get_window_size()
    x=size[‘width‘]
    y=size[‘height‘]
    return x,y

def swipe_up():
    #向上滑动
    size = get_size()
    x1=int(size[0]*0.5)
    y1=int(size[1]*0.9)
    y2=int(size[1]*0.1)
    driver.swipe(x1,y1,x1,y2,500)

def swipe_down():
    #向下滑动
    size = get_size()
    x1=int(size[0]*0.5)
    y1=int(size[1]*0.1)
    y2=int(size[1]*0.9)
    driver.swipe(x1,y1,x1,y2,500)

def swipe_left():
    #向左滑动
    size = get_size()
    x1=int(size[0]*0.9)
    x2=int(size[0]*0.1)
    y1=int(size[1]*0.5)
    driver.swipe(x1,y1,x2,y1,500)

def swipe_right():
    #向右滑动
    size = get_size()
    x1=int(size[0]*0.1)
    x2=int(size[0]*0.9)
    y1=int(size[1]*0.5)
    driver.swipe(x1,y1,x2,y1,500)

if __name__ == "__main__":

    print(get_size())
    for i in range(2):
        swipe_up()
        time.sleep(2)
        swipe_down()
        time.sleep(2)
        swipe_left()
        time.sleep(2)
        swipe_right()
        time.sleep(2)
