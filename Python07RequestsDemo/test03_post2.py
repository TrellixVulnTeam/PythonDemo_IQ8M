# 请求IHRM项目的登录接口，请求数据（{"mobile":"13800000002", "password":"123456"}）
# 登录接口URL：http://182.92.81.159/api/sys/login

# 导包
import requests

# 发送POST请求，请求体数据JSON格式
url = "http://182.92.81.159/api/sys/login"
login_data = {
    "mobile": "13800000002",
    "password": "123456"
}
response = requests.post(url, json=login_data)

# 获取响应结果
print("text=", response.text)
# json_data = response.json()
# print(type(json_data))
# print("json=", json_data)
