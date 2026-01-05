# Day 3 - Data Types & Conditions

# 1. 基本数据类型
score = 85  # int
price = 19.9  # float
name = "Python"  # str
is_pass = True  # bool
print(type(score))  # <class 'int'>
print(type(price))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_pass))  # <class 'bool'>

# 2. 容器类型
numbers = [1, 2, 3, 4]
person = {
    "name": "Tom",
    "age": 20
}
print(numbers)
print(person)

# 3. 条件判断
if score >= 90:
    print("成绩优秀")
elif score >= 60:
    print("成绩及格")
else:
    print("成绩不及格")

# 练习 1：成绩评级（用户输入）
stu_score = int(input("请输入成绩"))
if stu_score >= 90:
    print("成绩优秀，分数为", stu_score)
elif stu_score >= 60:
    print("成绩及格，分数为", stu_score)
else:
    print("成绩不及格，分数为", stu_score)

# 练习 2：简单权限判断
user = input("请输入(admin/user)")
if user == "admin":
    print("欢迎管理员")
else:
    print("欢迎用户")
