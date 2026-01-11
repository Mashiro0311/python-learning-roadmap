import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/house_data.csv', encoding="utf-8-sig")
df = df.dropna(how='all')
df = df.dropna(subset=["community", "area", "size", "price"])

df = df.reset_index(drop=True)
# 去掉"㎡"
df["size_sqm"] = (
    df["size"]
    .str.replace("㎡", "", regex=False)
    .astype(float)
)
# 去掉“万”
df["price_wan"] = (
    df["price"]
    .str.replace("万", "", regex=False)
    .astype(float)
)
# 计算单价（万 / ㎡）
df["price_per_sqm"] = df["price_wan"] / df["size_sqm"]
# 从地址中提取地区
df["area_dq"] = df["area"].str.partition('-')[0]
# print(df.head())
area_price = (
    df.groupby("area_dq")["price_per_sqm"]
    .mean()
    .sort_values(ascending=False)
)
print(area_price)

plt.scatter(df["size_sqm"], df["price_wan"])
plt.xlabel("Area (㎡)")
plt.ylabel("Total Price (万)")
plt.title("Size vs Total Price")
plt.show()

df["price_per_sqm"].plot(kind="hist", bins=20)
plt.xlabel("Price per ㎡ (万)")
plt.title("Price Distribution")
plt.show()

top_community = (
    df.groupby("community")["price_per_sqm"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(top_community)