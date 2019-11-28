"""
名片管理系统
1、程序启动，显示名片管理系统欢迎界面，并展示功能菜单
2、用户用数字选择不同的功能
3、根据功能选择，执行不同的功能
4、用户名片需要记录用户的姓名、电话、qq、邮件
5、如果查询到指定名片，用户可以选择修改或者删除名片
"""
print("*"*50)
print("欢迎使用名片管理系统v1.0")
print("1、新建名片")
print("2、显示全部")
print("3、查询名片")

print("0.退出系统")
print("*"*50)
card_list={}
num = input("请输入想选择的功能：")
if(num=="1"):
    print("-" * 50)
    name=input("请输入姓名：")
    card_list[name]={
        "tel": input("请输入电话："),
        "qq": input("请输入qq："),
        "邮件": input("请输入邮件：")
    }
    print("-" * 50)
elif(num=="2"):
    print("-" * 50)
    for n in card_list:
        print(card_list)
    print("-" * 50)
elif(num=="3"):
    print("-" * 50)
    find_card=input("请输入要查找的名片的名字：")
    if(find_card==card_list[find_card]):
        del card_list[find_card]
elif(num=="0"):
    print("退出系统")
    exit()



