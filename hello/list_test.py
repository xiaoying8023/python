# list是使用最频繁的数据类型，其他语言称为数组
# 专门用于存储一串信息，列表用[]定义，数据之间使用,分割，列表的索引（下标）从0开始

# 定义一个列表
name_list = ["zhangsan", "lucy", "jack"]
# 取数据
print(name_list[1])
# 列表常用操作（增删改查）,使用列表名加.,看可执行的操作
"""
增加：insert（索引，数据）    在指定位置插入数据
      append（数据）         在末尾追加数据
      extend（列表2）        将列表2的数据追加到列表
修改：列表[索引] = 数据       修改指定索引的数据
删除：del列表[索引]           删除指定索引的数据
      remove[数据]           删除第一个出现的指定数据
      pop                    删除末尾数据
      pop[索引]              删除指定索引数据
      clear                  清空列表
统计：len（列表）             列表长度
      count（数据）           数据在列表中出现的次数
排序：sort()                  升序排序
      sort（reverse=true）    降序排序
      reverse（）             逆序反转   
"""
# 确定数据在列表中的位置
# 查找
print(name_list.index("lucy"))
# 修改
name_list[0] = "tom"
# 增加
name_list.append("rose")
name_list.insert(1,"tim")
temp_list = ["li","lin"]
name_list.extend(temp_list)
print(name_list)
# 删除
# name_list.remove("rose")
# del name_list[0]
# name_list.pop(0)
# name_list.pop()
# name_list.clear()
# print(name_list)
# 统计
print(len(name_list))
print(name_list.count("tim"))
# 排序
name_list.sort()
print(name_list)
name_list.sort(reverse=True)
print(name_list)
name_list.reverse()
print(name_list)

# 循环遍历，使用for循环迭代遍历(顺序的从列表中一次保存数据)，
# 每一次循环都会保存在my_name这个变量中，在循环体内部可以访问当前这一次获取的数据
"""
for 变量 in 列表变量
    语句
"""
for my_name in name_list:
    print("我的名字叫：%s"%my_name)

# 应用场景
# 列表可以存储多个相同类型的数据