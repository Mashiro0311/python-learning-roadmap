# 文件读写 + 数据容器

import csv

# 1. 列表存多条数据
jobs = []
jobs.append("Python工程师")
jobs.append("Java工程师")
jobs.append("数据分析师")
print(jobs)

# 2. 字典存一条完整数据
job = {
    "title": "Python工程师",
    "salary": "20-30K",
    "city": "北京"
}
print(job)

# 3. 列表 + 字典组合（非常重要）
job_list = []
job_list.append({
    "title": "Python工程师",
    "salary": "20-30K",
    "city": "北京"
})
job_list.append({
    "title": "Java工程师",
    "salary": "20-30K",
    "city": "上海"
})
print(job_list)
for j in job_list:
    if j["title"] == "Java工程师":
        continue
    print("-----------------------------岗位信息--------------------------------")
    print("职位：", {j["title"]}, "\n工资：", {j["salary"]}, "\n城市：", {j["city"]})
    print("--------------------------------------------------------------------")

# 4. 文件写入（CSV 思维）

headers = ["title", "salary", "city"]
filename = "jobs.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(job_list)
    f.close()
print("数据已经写入到", filename)
