"""
字典：内置的数据结构，用于存储键值对。每个键在字典中是唯一的，并与一个值相关联
语法格式：变量名 = {键1：值1，键2：值2，。。。}
注：1.字典的所有键值对（元素）被放置在一对{}花括号中，键与值之间使用冒号：进行分隔，而键值对（元素）之间使用逗号，进行分隔
   2.在字典中，每个键都是唯一的，用于唯一标识一个值，但同一个值可以被多个不同的键所关联，即值可以重复
（键名唯一，但键所对应的值可以重复，如果重复前面的键值会被后面的键值覆盖）
"""
# info = {"name":"xiaohua","str":"xiaohua","list":[1,2,3],"list":(1,2,3)}
# # 注：变量名要加双引号等标识，否则变量名无法正常输出，只输出字符类型
# # {<class 'int'>: 1, <class 'str'>: 'bingbing', <class 'list'>: (1, 2, 3)}
# #{'name': 'xiaohua', 'str': 'xiaohua', <class 'list'>: (1, 2, 3)}
# #键名唯一，但键所对应的值可以重复，如果重复前面的键值会被后面的键值覆盖
# print(info)

"""字典常见操作
1.查看元素
（1）in：只是检查键（非键值）是不是在字典中，是，返回Ture；否则，返回False
（2）not in：只是检查键（非键值）是不是在字典中，不是，返回Ture；否则，返回False
（3）len():检查字典的长度（键值对数）
（4）dict[key]:根据键来获取字典中对应的值。如果指定的键存在字典中不存在，报错（keyError）
     key:查找的键（字典中不存在下标，输入键名，得到键值）
（5）get(key,default):根据键来获取字典中对应的值。如果指定的键在字典中不存在，
则返回指定的默认值（如果提供的话），如果没有制定刚刚默认值，则返回None.
        dict.get(key,default)
   key:要查找的键
   default(可选):当字典中不存在指定的键，则返回的值。默认为None
"""
'''in检查的是字典中的键，而非键值'''
# info = {"name":"xiaohua","str":"xiaohua"}
# print("name" in info)  # True
# print("nbingbing" in info)  # False

# print("name" not in info)  # False
# print("nbingbing" not in info)  # True
#
# print(len(info))  # 2
'''dict[]:查找键名对应键值'''
# info = {"name":"xiaohua","str":"xiaohua"}
# print(info["name"])
#
# print(info.get("ste", 1) ) # xiaohua  1
# print(info.get("shui"))  #  None

'''2.修改（添加）元素：修改键所对应的键值（添加与修改的区别在于键名是否存在 ）
dict[key] = value   
  info["str"]= "shuihua"
key:要修改的键
Value:要修改的键相关联的值
'''
# info = {"name":"xiaohua","str":"xiaohua"}
# info["str"]= "shuihua"  # {'name': 'xiaohua', 'str': 'shuihua'}
# # 字典存在——修改
# info["tua"]= "xiaohua"  # {'name': 'xiaohua', 'str': 'shuihua', 'tua': 'xiaohua'}
# # 字典不存咋——添加
# print(info)

"""3.删除元素
（1）del:根据键删除字典中的元素（键值对），如果尝试删除一个不存在键，则报错（keyError)
del dict[key] 
key:要删除的键。这个键需要存在，不存在，删除报错
（2）clear（）：删除字典中的所有元素（键值对），将其变为空字典
语法格式：dict.clear()
（3）pop(key,default):从字典中移除指定的键以及其对应的值，并返回被移除的值。
如果指定键不存在，并且也没有提供默认值，将报错。若存在默认值，增不存在时返回该值
   dict.pop(key,default)
key:要移除的键
default(可选):若不存咋键，则返回此致。若未提供且键不存在，报错
见下： info.pop("hua",1)  #无反应
      print(info.pop("hua",1))  # 报错，返1
      
"""

'''del dict[key]'''
# info = {"name": "xiaohua", "str": "xiaohua"}
# del info["str"]
# del info["huo"]  # 报错
# print(info)
'''dict.clear()'''
# info.clear()
# print(info)
'''dict.pop(key,default)'''
# info = {"name": "xiaohua", "str": "xiaohua"}
# info.pop("name")  # {'str': 'xiaohua'}
# info.pop("hua")  # 报错
# info.pop("hua",1)   # 无反应
# print(info.pop("hua",1))  # 报错，返回1

'''4.遍历字典
(1)for in :默认遍历所有的键名
(2)dict.keys():获取字典所有键（键名）的视图对象，这个视图对象支持迭代，但本身不是列表或
或任何可以直接进行索引访问的数据结构
(3)dict.values():获取字典所有键（键值）的视图对象，这个视图对象支持迭代，但本身不是列表或
或任何可以直接进行索引访问的数据结构
(4)items():获取字典中所有键值对（键名与键值）的视图对象，这个视图对象支持迭代，但本身不是列表或
或任何可以直接进行索引访问的数据结构
注：字典视图对象是动态的，若元字典发生变化，那么通过方法获得的视图也会相应地更新
'''
# info = {"name": "xiaohua", "str": "xiaohua"}
# for i in info:
#     print(i)
'''dict.keys():依次取出键名'''
# info = {"name": "xiaohua", "str": "xiaohua"}
# keys_views = info.keys()
# print(keys_views,type(keys_views))  # dict_keys(['name', 'str']) <class 'dict_keys'>
# for i in keys_views:
#     print(i)  # 依次取出键名
'''dict.value():依次取出键值'''
# info = {"name": "xiao", "str": "hua"}
# values_views = info.values()
# print(values_views, type(values_views))  # dict_keys(['name', 'str']) <class 'dict_keys'>
# for i in values_views :
#     print(i)  # 依次取出键值
'''dict.items():依次取出键值对'''
info = {"name": "xiao", "str": "hua"}
items_views = info.items()  # dict_items([('name', 'xiao'), ('str', 'hua')])
print(items_views)
for i in items_views:  # ('name', 'xiao')  ('str', 'hua')
    print(i)

print(items_views)  # 字典视图对象是动态的，若元字典发生变化，那么通过方法获得的视图也会相应地更新



