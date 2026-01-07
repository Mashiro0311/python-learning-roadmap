import csv
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
    blocks = soup.find_all("div", class_="quote")
    for block in blocks:
        quote = block.find("span", class_="text").text
        author = block.find("small", class_="author").text
        all_quotes.append({
            "quote": quote,
            "author": author
        })
    # print(all_quotes)
    print(f"第 {i} 页抓取完成，当前共 {len(all_quotes)} 条")
with open("quotes.csv", "w", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(all_quotes)
    f.close()

print("数据已成功保存为 quotes.csv")
print("==========")
print("爬取结束，总条数：", len(all_quotes))
