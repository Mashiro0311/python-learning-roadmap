# https://www.python.org/jobs/
import requests
import csv
import time
from bs4 import BeautifulSoup

BASE_URL = 'https://www.python.org/jobs/?page={}'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}


def extract_company(tag):
    if not tag:
        return ""
    return list(tag.stripped_strings)[-1]


def safe_text(tag, default=""):
    try:
        return tag.get_text(strip=True)
    except:
        return default


def crawl_jobs(page):
    url = BASE_URL.format(page)
    response = requests.get(url, headers=HEADER, timeout=5)
    if response.status_code != 200:
        print(f"第 {i} 页请求失败")
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    jobs = soup.select('ol.list-recent-jobs li')
    # print(jobs)
    page_data = []
    for job in jobs:
        title = safe_text(job.select_one("h2 a"))
        # print(title)
        company = extract_company(job.select_one(".listing-company-name"))
        location = job.select_one(".listing-location")
        time_tag = job.select_one("time")
        page_data.append({
            'title': title,
            'company': company,
            'location': location.text.strip() if location else "",
            'time_tag': time_tag["datetime"] if time_tag else ""
        })
    return page_data


def save_to_csv(data, filename):
    with open(filename, "w", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "company", "location", "time_tag"])
        writer.writeheader()
        writer.writerows(data)
    print(f"数据已保存到 {filename}")


def main():
    all_jobs = []
    for page in range(1, 3):
        print(f"正在爬取第{page}页")
        data = crawl_jobs(page)
        all_jobs.extend(data)
        time.sleep(1)
    print(f"共{len(all_jobs)}条数据")
    save_to_csv(all_jobs, "all_jobs.csv")


if __name__ == '__main__':
    main()