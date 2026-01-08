import csv
import time

import requests
import random
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com/page/{}/"
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]
HEADERS = {
    "User-Agent": random.choice(USER_AGENTS)  # 随机 User-Agent
}


def crawler_page(page):
    url = BASE_URL.format(page)
    response = requests.get(url, headers=HEADERS, timeout=10)
    if response.status_code != 200:
        print(f"第 {page} 页请求失败,状态码：{response.status_code}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    blocks = soup.find_all("div", class_="quote")
    page_data = []
    for block in blocks:
        quote_tag = block.find("span", class_="text")
        author_tag = block.find("small", class_="author")
        if not quote_tag or not author_tag:
            continue
        page_data.append({
            "quote": quote_tag.text.strip(),
            "author": author_tag.text.strip()
        })
    return page_data


def main(total_page, filename):
    all_quotes = []
    for page in range(1, total_page + 1):
        try:
            page_data = crawler_page(page)
            all_quotes.extend(page_data)
            print(f"第 {page} 页完成，累计 {len(all_quotes)} 条")
            time.sleep(random.uniform(1, 2))  # 请求间隔
        except Exception as e:
            print(f"第{page}页出错：", e)

    save_to_csv(all_quotes, filename)


def save_to_csv(data, filename):
    with open(filename, "w", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=['quote', 'author'])
        writer.writeheader()
        writer.writerows(data)
    print(f"数据已经保存到：{filename}")


if __name__ == '__main__':
    t_page = 4
    f_name = "quotes_crawl.csv"
    main(t_page, f_name)
