
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