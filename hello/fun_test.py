
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
