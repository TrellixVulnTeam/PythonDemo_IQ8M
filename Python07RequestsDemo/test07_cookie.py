# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login
# 我的订单：http://localhost/Home/Order/order_list.html

import requests

# 获取验证码
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print("cookies=", response.cookies)
PHPSESSID = response.cookies.get("PHPSESSID")
print("PHPSESSID==", PHPSESSID)

# 登录
login_data = {
    "username": "13012345678",
    "password": "123456",
    "verify_code": "8888",
}
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
respone = requests.post(url, data=login_data, cookies={"PHPSESSID": PHPSESSID})
print("json_data=", respone.json())

# 我的订单
response = requests.get("http://localhost/Home/Order/order_list.html", cookies={"PHPSESSID": PHPSESSID})
print("text=", response.text)



