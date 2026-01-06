import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com/page/{}/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

all_quotes = []

for i in range(1, 4):
    url = BASE_URL.format(i)
    print(f"正在抓取第{i}页，URL：{url}")
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"{url}请求失败，状态码：{response.status_code}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    for q in quotes:
        all_quotes.append(q.text)
    print(f"第 {i} 页抓取完成，当前共 {len(all_quotes)} 条")
print("==========")
print("爬取结束，总条数：", len(all_quotes))