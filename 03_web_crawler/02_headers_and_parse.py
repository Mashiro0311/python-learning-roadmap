# 为什么必须加 headers？
# 因为很多网站会拒绝“不像浏览器”的请求
import requests
from bs4 import BeautifulSoup

url1 = "https://httpbin.org/headers"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url1, headers=headers)
print(response.text)  # 服务器收到 User-Agent, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# HTML 解析
url = "https://quotes.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")
print(soup)
# 解析数据
quotes = soup.find_all("span", class_="text")  # 定位

data = []

for q in quotes:
    data.append({
        "quote": q.text
    })
print(f"共抓取了{len(data)}条数据")
