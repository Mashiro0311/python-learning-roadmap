import pandas as pd
import re

try:
    df = pd.read_csv("all_jobs.csv", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("all_jobs.csv", encoding="gbk")
df = df.dropna(how="all")
print(df.head())
print(df.info())

top_company = (
    df["company"]
    .value_counts()
    .head(10)
)
print(top_company)

df["is_python"] = df["title"].str.contains(
    "Python", case=False, na=False
)
python_rate = df["is_python"].mean()
print(f"Python 岗位占比：{python_rate:.2%}")

experience_count = df["experience"].value_counts()
print(experience_count)

location_count = df["location"].value_counts().head(10)
print(location_count)


# def parse_salary(s):
#     if pd.isna(s):
#         return None
#     nums = re.findall(r"\d+", s)
#     if len(nums) >= 2:
#         return (int(nums[0]) + int(nums[1])) / 2
#     return None


df["salary_avg"] = df["salary"]

print(df["salary_avg"].describe())
