
def multiple_table():
    # 函数初次建立
    # 打印九九乘法表
    m = 1
    n = 1
    num = 0
    while m <= 9:
        n = 1
        while n <= m:
            num = m * n
            print("%d*%d=%d " % (n, m, num), end="")
            n += 1
        m += 1
        print("")


def sum(a,b):
    sum = a+b
    print(sum)
    return sum
# 求平方根
num = 4**0.5
print(num)

#交换连个数
#1、使用中间变量交换
a=6
b=200
c=a
a=b
b=c
#2、不使用中间变量交换
a=a+b
b=a-b
a=a-b
#3、python独有的交换方式
a,b=b,a
print(a,b)


#多值参数
def demo(num,*nums,**person):
    print (num)
    print (nums)
    print (person)

demo(1,name="小明",age=18)
#*args代表元组，**args代表字典
def sun_num(*args):
    num=0
    print (args)
    for n in args:
        num+=n
    print (args)
    return num
result = sun_num(1,2,3)
print (result)
#元组和字典拆包
#调用参数时，在参数前加一个*，是元组，加两个*是字典

#递归
def sum_fun(num):
    print (num)
    if num==1:
        return
    sum_fun(num-1)
sum_fun(3)




