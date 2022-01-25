# 使用requests库调用TPshop登录功能的相关接口，完成登录操作
# 登录成功后获取‘我的订单’页面的数据
# 要求：使用Session对象来实现
# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login
# 我的订单：http://localhost/Home/Order/order_list.html

# 导包
import requests

# 创建Session对象
session = requests.Session()

# 获取验证码
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
print("cookies=", response.cookies)

# 登录
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "13012345678",
    "password": "123456",
    "verify_code": "8888",
}
response = session.post(url, data=login_data)
print("json data=", response.json())

# 我的订单
response = session.get("http://localhost/Home/Order/order_list.html")
print("text=", response.text)

# 关闭Session对象
session.close()


