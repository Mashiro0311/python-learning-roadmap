# HTTP 请求
import requests

url = "https://httpbin.org/get"
response = requests.get(url)  # 发送请求
print(response.status_code)  # 状态码
print(response.text)  # 文本

params = {
    "page": 1,
    "size": 10
}

response = requests.get(url, params=params)  # 添加参数
print(response.url)  # https://httpbin.org/get?page=1&size=10
