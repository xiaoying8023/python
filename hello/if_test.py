a = 2
if a < 10:
    a = 10
    print(a)

age = int(input("请输入年龄："))
if age>=18:
    print("允许进入")
else:
    print("禁止进入")


if age >= 17 and a <= 19:
        print("ok")
elif age <= 17 or age >= 19:
        print("no")

is_employee = False
if not is_employee:
    print("非本公司人员")

holiday_name = input("请输入今天的节日：")
if holiday_name == "情人节":
    print ("买玫瑰")
    print ("看电影")
elif holiday_name == "平安夜":
    print("送苹果")
    print("吃大餐")
elif holiday_name == "生日":
    print ("生日礼物")
else:
    print ("快乐每一天")

player = int(input("请输入您要出的石头1剪刀2布3"))
computer = 1
print ("玩家出的是：%d"%player)
if ((player == 1 and computer == 2)
    or (player ==2 and computer==3)
    or (player==3 and computer)==1):
    print("玩家赢了")
elif player == computer:
    print("再来一局")
else:
    print ("继续")

import random
print (random.randint(1,3))
computer = random.randint(1,3)
if ((player == 1 and computer == 2)
    or (player ==2 and computer==3)
    or (player==3 and computer)==1):
    print("玩家赢了")
elif player == computer:
    print("再来一局")
else:
    print ("继续")



