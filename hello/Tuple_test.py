"""
# 元组（Tuple）与列表类似,但是元组的元素不能修改
  元组表示多个元素组成的序列
# 元组使用（）定义，使用,分开，索引从0开始；只有一个数据时，需要在元素后面加逗号
# 元组有特定的应用场景，元组可以保存不同类型的数据。
"""
# 创建空元组
tuple1 = ()
tuple2 = ("tom", 18, 166)
print(type(tuple2))
# 使用中括号取数据
print(tuple2[1])
single_tuple = (5)
# single_tuple并不是一个元组，是整型
print(type(single_tuple))
# 定义只包含一个元素的元组
single_tuple2 = (5,)
# 元组的常用操作
info = ()
"""
查询： index    取索引
       count    统计计数
与列表完全相同
"""
print(tuple2)
print(tuple2[0])
print(tuple2.count(18))
print(tuple2.index("tom"))

# 遍历
for item in tuple2:
    print(item)

# 应用场景
# 函数的参数和返回值
# 格式字符串
# 保护列表数据安全

# 格式化字符串
stu_tuple = ("小明",17,185)
# 格式化字符串后面的（）实质上就是元组
print("%s年龄是%d身高是%0.0f"%stu_tuple)
stu_tuple = "%s年龄是%d身高是%0.0f"%stu_tuple
print(stu_tuple)

# 元组与列表转换
num_list = [1, 2, 3, 4]
num_tuple = tuple(num_list)
num_list = list(num_tuple)




