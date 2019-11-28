# 公共方法
"""
1、python内置函数
len(item) 计算容器中元素个数
del(item)   删除变量
max(item)   返回容器中元素最大值
min(item)   返回容器中元素最小值


"""

list1 = [1, 2]
list1.extend([3, 4])
print(list1)
list1.append([5, 6]) # append会把加入的数据在列表中当作一个元素
print(list1)

"""
成员运算符
in
not in
"""
print("A" in "ABCD")
# in查询字典的键
"a" in{"a": "lao"}

"""
#完整的for循环语法
for 变量 in 集合:
    循环体代码
else:
    没有通过break退出循环，循环结束后，会执行的代码
"""

for num in [1,2,3]:
    print(num)
    if(num==2):
        break
else:
    print("会执行吗")
print("循环结束")

students = [
    {"name": "阿土"},
    {"name": "tom"}

]
find_name="阿土"
for stu in students:
    print(stu)
    if(stu["name"]==find_name):
        print("查找成功 %s"% find_name)
        break
else:
    print("没有")
