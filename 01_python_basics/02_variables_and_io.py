# Day 2 - Variables & Input / Output

# 1. 变量
name = "Python Learner"
age = 18

print("Name:", name)
print("Age:", age)

# 2. 输入
user_name = input("请输入你的名字：")
user_age = input("请输入你的年龄：")
print("你好", user_name)
print("明年你将", int(user_age) + 1, "岁。")  # input得到的是字符串 年龄需要做转型

# 练习 1：个人信息卡
# 要求：
# - 使用变量
# - 使用 input
# - 打印完整信息
u_name = input("请输入你的名字：")
u_age = input("请输入你的年龄：")
city = input("你所在的城市：")
job = input("你的职业：")

print("—— 个人信息卡 ——")
print("姓名：", u_name)
print("年龄：", u_age)
print("城市：", city)
print("职业：", job)
