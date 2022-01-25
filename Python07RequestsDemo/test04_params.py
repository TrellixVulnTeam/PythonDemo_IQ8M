# 访问百度的搜索接口，通过查询字符串的方式传递搜索的关键字python，并查看响应数据
# 请求路径格式为：http://www.baidu.com/s?wd=python

# 导包
import requests

# 发送请求
# 直接定义在URL中
# response = requests.get("http://www.baidu.com/s?wd=python")

# 传递字符串方式的参数
# response = requests.get("http://localhost/Home/Goods/search.html", params="q=iPhone&name=tom")

# 传递字典类型的参数
response = requests.get("http://localhost/Home/Goods/search.html", params={"q": "iPhone", "name": "tom"})

# 获取响应数据
# print("text=", response.text)
print("url", response.url)
