# str1="最美的不是下雨天"
# str2= '最美的不是"下雨天"'
# print (str2)
# print (str1[3])
# for s in str2:
#     print (s, end="")
# # 字符串长度
# len(str2)
# #某个字符（子串）出现的次数
# # count("最")
# # 某个子串出现的位置
# str2.index("的不是")

# 字符串常用方法
"""
1、判断类型

"""


num = [23, 1, 21, 66, 95, 3, 55, 76, 12, 89]
n = 0
temp = 0
while n < 10:
    m = 0
    while m < 10-n-1:
        if num[m] > num[m+1]:
            temp = num[m+1]
            num[m+1] = num[m]
            num[m] = temp
        m += 1

    n += 1
print(num)

