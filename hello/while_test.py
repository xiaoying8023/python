
# while循环练习
i = 0
while i < 3 :
    print ("hello")
    i+=1
sum = 0
sum_oushu = 0
sum_jishu = 0
i = 0
while i <= 100:
    sum = sum + i

    if i % 2 == 0:
        sum_oushu += i
    else : sum_jishu += i
    i += 1
print (sum)
print (sum_jishu)
print (sum_oushu)
#输出*下三角
row = 1
while row <= 5:
    column =0
    while column < row:
        print("*", end="")
        column +=1
    row += 1
    print("")
#打印九九乘法表
m = 1
n = 1
num = 0
while m <= 9:
    n=1
    while n <= m:
        num = m*n
        print("%d*%d=%d " %(n,m,num), end="")
        n += 1
    m += 1
    print("")




