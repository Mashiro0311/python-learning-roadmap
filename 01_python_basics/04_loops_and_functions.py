# Day 4-5 - Loops & Functions (Sprint)

# 1. for 循环
for i in range(5):
    print("for循环：", i)

# 2. while 循环
count = 0
while count < 10:
    print("while循环：", count)
    count += 1  # while循环中必须要给一个叠加不然就是死循环

# 3. break / continue
for i in range(10):
    if i == 5:
        break
    print("break示例：", i)

for i in range(20):
    if i == 2:
        continue
    print("continue示例", i)


# 4. 定义函数
def greet(name):
    return f"你好{name}"


msg = greet("Python学习者")
print(msg)


# 简易计算器（控制台版）
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("=== 简易计算器 ===")
number1 = int(input("请输入一个数字："))
number2 = int(input("请再输入一个数字："))
fuhao = input("请输入符号（+，-，*，/）：")
if fuhao == "+":
    print(add(number1, number2))
elif fuhao == "-":
    print(sub(number1, number2))
elif fuhao == "*":
    print(mul(number1, number2))
elif fuhao == "/":
    print(div(number1, number2))
else:
    print("请输入正确的运算符")
