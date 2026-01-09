# jobs_crawler
一个基于 Python 的入门级爬虫
用于爬取 https://www.python.org/jobs/ 的招聘信息，并进行简单统计分析。

## 📌 项目功能

- 爬取多页数据
- 提取岗位、公司、地址、时间
- 保存为 CSV 文件
- 使用 pandas 进行数据统计分析

## 🛠 使用技术

- Python 3
- requests
- BeautifulSoup
- pandas
- CSV

## 🧠 学习收获
### 爬虫
- 发现“字段污染”问题
- 追求 数据质量
### 数据处理
- 去除全空行及关键字段缺失数据
- 解析薪资区间并转换为数值
- 字段清洗与标准化处理

