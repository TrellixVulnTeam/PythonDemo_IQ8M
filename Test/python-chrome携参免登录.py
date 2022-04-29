""""
携带chrome本地cookie登录实现免登陆操作
注意：需要保证没有chrome浏览器正在打开，否则运行报错!!!
个人资料路径(chrome://version/，查看个人资料路径,去掉最后的‘\Default’)
"""
from time import sleep

from selenium import webdriver


def get_cookie(url):
    profile_directory = r'--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data'
    # 加载配置数据
    option = webdriver.ChromeOptions()
    option.add_argument(profile_directory)
    # 启动浏览器配置
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)
    # 等待时间
    sleep(5)
    # 退出驱动
    driver.quit()


if __name__ == '__main__':
    # url = 'https://www.baidu.com'
    url = 'https://weibo.com/'
    get_cookie(url)
