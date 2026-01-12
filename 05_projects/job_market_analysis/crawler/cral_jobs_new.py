import random
import time
from urllib.parse import quote
from playwright.sync_api import sync_playwright, TimeoutError
from db import insert_job  # 数据库写入函数


# ----------------- 响应处理 -----------------
def handle_response(response, keyword):
    if "api/job/search-pc" in response.url:
        try:
            data = response.json()
            items = data.get("resultbody", {}).get("job", {}).get("items", [])
            if not items:
                print("⚠️ 当前响应没有职位列表")
                return

            for item in items:
                job_info = {
                    "job_name": item.get("jobName"),
                    "company": item.get("companyName"),
                    "city": item.get("jobAreaString"),
                    "salary": item.get("provideSalaryString"),
                    "experience": item.get("workYearString"),
                    "education": item.get("degreeString"),
                    "skills": ",".join(item.get("jobTagsForOrder", [])),
                    "keyword": keyword
                }
                try:
                    insert_job(job_info)
                    print(f"✅ 写入职位: {job_info['job_name']} - {job_info['company']} (关键词: {keyword})")
                except Exception as e:
                    print("❌ 插入数据库失败:", e)
        except Exception as e:
            print("❌ JSON 解析失败:", e)
            try:
                print(response.text()[:500])
            except Exception as e2:
                print("❌ 获取文本失败:", e2)


# ----------------- Playwright 主流程 -----------------
keywords = ["文员"]  # 可自定义关键词列表

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    )

    for keyword in keywords:
        print(f"\n🔍 开始抓取岗位: {keyword}")
        page = context.new_page()
        page.on("response", lambda resp, kw=keyword: handle_response(resp, kw))

        keyword_encoded = quote(keyword)
        page.goto(f"https://we.51job.com/pc/search?keyword={keyword_encoded}", timeout=60000)

        # 等待职位列表加载
        try:
            page.wait_for_selector(".joblist", timeout=30000)
        except TimeoutError:
            print("⚠️ 职位列表加载超时")

        # ----------------- 自动翻页循环 -----------------
        page_number = 1
        while True:
            print(f"⏳ 第 {page_number} 页等待页面数据加载...")
            time.sleep(random.uniform(5, 8))  # 等待当前页的响应完全处理

            # 下一页按钮
            try:
                next_btn = page.query_selector("button.btn-next")
                if next_btn:
                    class_attr = next_btn.get_attribute("class") or ""
                    # ✅ 正确判断最后一页
                    if next_btn.is_disabled():
                        print(f"✅ {keyword} 已到最后一页（共 {page_number} 页）")
                        break
                    else:
                        print(f"➡️ {keyword} 点击下一页")
                        next_btn.click()
                        page_number += 1
                        try:
                            page.wait_for_selector(".joblist", timeout=20000)
                        except TimeoutError:
                            print("⚠️ 下一页职位列表加载超时，等待 5~10 秒后继续")
                            time.sleep(random.uniform(5, 10))
                else:
                    print(f"❌ {keyword} 未找到下一页按钮，结束翻页")
                    break
            except Exception as e:
                print(f"❌ {keyword} 翻页失败:", e)
                break

        page.close()
        print(f"✅ {keyword} 抓取完成")

    print("🎉 所有岗位抓取完成，浏览器即将关闭")
    browser.close()
