# Quotes Crawler & Analysis

一个基于 Python 的入门级爬虫 + 数据分析项目  
用于爬取 quotes.toscrape.com 的名言数据，并进行简单统计分析。

## 📌 项目功能

- 爬取多页名言数据（支持页数配置）
- 提取名言内容与作者
- 保存为 CSV 文件
- 使用 pandas 进行数据统计分析

## 🛠 使用技术

- Python 3
- requests
- BeautifulSoup
- pandas
- CSV

## 📂 项目结构

├── crawler.py        # 爬虫脚本  
├── analysis.py       # 数据分析脚本  
├── quotes.csv        # 爬取结果  
└── README.md         # 项目说明  

## 🚀 使用方法

### 1. 安装依赖
```bash
pip install requests beautifulsoup4 pandas
```
### 2.运行爬虫
```bash
python crawler.py
```
### 3.数据分析
```bash
python analysis.py
```

## 📊 示例分析结果

- 名言数量最多的作者：Albert Einstein
- 可对作者分布进行进一步分析和可视化

## 🧠 学习收获

- 掌握基础网页爬取流程
- 学会将数据结构化保存
- 初步理解数据分析思路
- 具备简单项目工程结构意识