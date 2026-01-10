import time

import requests
import csv
from bs4 import BeautifulSoup

BASE_URL = 'https://beijing.anjuke.com/sale/p{}/'

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}


def safe_text(tag):
    return tag.get_text(strip=True) if tag else ""

def crawler_house(page):
    url = BASE_URL.format(page)
    response = requests.get(url, headers=HEADER, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        blocks = soup.find_all('div', class_='property')
        # print(blocks)
        page_data = []
        for block in blocks:
            try:
                title = safe_text(block.find('h3', class_='property-content-title-name'))
                community = block.find('p', class_='property-content-info-comm-name').text.strip()
                area_tag = block.find('p', class_='property-content-info-comm-address')
                area = list(area_tag.stripped_strings)
                size_tag = block.find('div', class_='property-content-info')
                size_list = list(size_tag.stripped_strings)
                size = next((s for s in size_list if "㎡" in s), "")
                price_tag = block.find('p', class_='property-price-total')
                price = list(price_tag.stripped_strings)
                page_data.append({
                    'title': title,
                    'community': community,
                    'area': '-'.join(area),
                    'size': size,
                    'price': ''.join(price)
                })
            except Exception as e:
                continue
        return page_data
    else:
        print(f"访问失败，错误码：{response.status_code}")
        return []


def save_to_csv(page_data, filename):
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'community', 'area', 'size', 'price'])
        writer.writeheader()
        writer.writerows(page_data)
        print(f"成功写入文件{filename}")


def main(page_total, filename):
    all_data = []
    for page in range(1, page_total + 1):
        print(f"正在爬取第{page}页")
        data = crawler_house(page)
        all_data.extend(data)
        time.sleep(2)
    print(f"共{len(all_data)}条数据")
    save_to_csv(all_data, filename)


if __name__ == '__main__':
    main(5, '../data/house_data.csv')
