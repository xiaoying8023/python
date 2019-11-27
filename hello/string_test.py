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
isspace()    如果string中只包含空格，则返回true
isalnum()   如果string至少有一个字符并且所有字符都是字母或数字则返回True
isdecimal() r如果string只包含数字则返回True,全角数字
isalpha()   如果string至少有一个字符并且所有字符都是字母则返回True
isdigit()   如果string只包含数字则返回True,全角数字、（1）、\u00b2
isnumberic() 如果string只包含数字则返回True,全角数字，汉字数字
istitle()   如果string是标题化的（每个单词的首字母大写），则返回True
islower()   如果string中包含至少一个区分大小写的字符，并且所有这些（区分大小写的）字符都是小写，则fanhuiTrue
isUpper()   如果string中包含至少一个区分大小写的字符，并且所有这些（区分大小写的）的字符都是小写，则返回True

2、查找和替换
startswith(str) 检查字符串是否是以str开头，是则返回True
endswith(str)   检查字符串是否是以str结束，是则返回True
find(str,start=0,end=len(string))   类似于find()函数，不过是从右边开始查找
index(str,start=0,end=len(string))  跟find（）方法类似，只不过如果str不在string会报错
rindex(str,start=0,end=len(strng))  类似于index(),不过是从右边开始
replace(old_str,new_str,num=string.count(old))  把string中的old_Str替换成new_str，如果num指定，则替换不超过num次

3、大小写转换
capitalize()    把字符串的第一个字符大写
title()     把字符串的每个单词首字母大写
lower()     转换string中多有大写字符为小写
upper()     转换string中的小写字母为大写
swapcase（）  翻转string中的大小写

4、文本对齐
ljust(width)    返回一个原字符串左对齐，并使用空格填充至长度width的新字符串
rjust(width)     返回一个原字符串右对齐，并使用空格填充至长度width的新字符串
center(width)     返回一个原字符串居中，并使用空格填充至长度width的新字符串

5、去除空白字符
lstrip()    截掉string左边（开始）的空白字符
rstrip()    截掉string右边（末尾）的空白字符
strip()     截掉string左右两边的空白字符
6、拆分和连接
partition(str)     把字符串string分成一个3元素的元组（str前面，str,str后面）
rpartition(str)    类似于partition()函数，不过是从右边开始查找
split(str="",num)   以str为分隔符切片string,如果num有指定值，则仅分隔num个子字符串，str默认包含‘r’,'\t','\n'和空格
splitlines()        按照行（'\r','\n','\r\n'）分隔，返回一个包含各行作为元素的列表
join（seq)           以string作为分隔符，将seq中所有的元素（的字符串表示）合并为一个新的字符串


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

