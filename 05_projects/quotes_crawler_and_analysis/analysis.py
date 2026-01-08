import pandas as pd

# 1.读取数据
df = pd.read_csv('quotes.csv')  # 读取CSV文件
print(df.head())  # 读取钱5行数据
print("总数据量：", len(df))

# 2.基础统计
author_count = df['author'].value_counts()  # 这是最经典的数据分析操作之一
print("名言数量最多的作者（前 5）：")
print(author_count.head())

# 3. 简单“结论型输出”
top_author = author_count.idxmax()
top_count = author_count.max()
print(f"名言最多的作者是：{top_author}，共有 {top_count} 条名言")
