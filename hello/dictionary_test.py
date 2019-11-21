"""
字典是除列表以外Python中最灵活的数据类型
通常存储一个物体的相关信息，是无序的对象集合
字典使用键值对存储数据，键值对之间使用,分隔
键key是索引，值value是数据，键值之间使用：分开
键必须是唯一的，键只能使用字符串、数字、元组，值可以使任何数据类型
xiaoming = {"name":"小明","age":"18","gender":True,"height":175}
"""
student={"name": "liyang", "age": 22,"gender": True}
print (student)
# 字典的常用操作
"""
1、取值
xiaoming[name],使用key取值
如果指定的key不存在会报错

2、增加/修改
增加：xiaoming["age"]=18
修改：xiaoming["name"]="xyz"
如果key存在，会修改已经存在的键值对

3、删除
xiaoming.pop(key)

4、统计键值对的数量
len(xiaoming)

5、合并字典
temo_dict = {"height":175}
xiaiming.update(temp_dict)
如果键存在，会更新键对应的值
6、清空字典
xiaoming.clear()

循环遍历
for k in xiaoming :
    printf("%s:%s"%(k,xiaoming[k]))
"""
xiaoming={"name":"小明", "qq":1245, "phone":"123489"}
for k in xiaoming:
    #k是每次循环获取到的键值key
    print("%s:%s"%(k,xiaoming[k]))

"""
应用场景：
    使用多个键值对描述一个物体的相关信息
    将多个字典放在一个列表中，再进行遍历，在循环体内部针对每一个字典进行相同的处理
"""

card_list = [
    {"name":"李阳", "age":"21", "gender": True},
    {"name":"李辉", "age":21,"gender":True}
]
for card_list in card_list:
    print (card_list)
