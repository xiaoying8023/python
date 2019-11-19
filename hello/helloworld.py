# 第一个注释
print("hello,python")
print("hello,world")
# 记录账号
number = "123"
# 记录密码
password = "123"
print(password, number)
price = 8.5
weight = 7.5
money = price * weight
money = money - 5
print(money)
"""
姓名：小明
年龄：18
性别：男生
身高：175
体重：150
"""
name = "小明"
age = 18
sex = "男"
ss = True
height = "175"
weight = "187"
print(name,age,sex,height,weight,ss)
print(type(age))

zhang = "张"
san = "三"
print(zhang+san)
print((zhang+san)*10)
name1 = input("请输入名字：")
print(name1)

# 输入苹果的单价
price1_str = input("单价:")
# 输入苹果重量
weight_str = input("重量:")
# 计算 注意两个字符串变量之间不能直接用乘法
money_str = float(price1_str)*float(weight_str)
print(money_str)
# 格式化输出
print("我的名字叫%s"%name)

import keyword
print(keyword.kwlist)