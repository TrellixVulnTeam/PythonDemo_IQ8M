# 请求IHRM项目的登录接口，URL：http://182.92.81.159/api/sys/login
# 请求头：Content-Type: application/json
# 请求体：{"mobile":"13800000002", "password":"123456"}


# 导包
import requests

# 发送请求
login_data = '{"mobile": "13800000002", "password": "123456"}'
header_data = {
    "Content-Type": "application/json"
}
response = requests.post("http://182.92.81.159/api/sys/login", data=login_data, headers=header_data)

# 获取响应数据
print(response.json())
