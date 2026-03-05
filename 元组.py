"""元组内置数据结构，用于存储一系列的元素，与列表的主要区别在于元组不可变的
元组一旦创建，不能更改它的内容，通常用于存储一些不应该被改变的数据集合，比如一周的天数‘
等
   语法格式：变量名 = （元素1，元素2，元素3，...）
注：1.元组的所有元素被有序的放置在一对小括号内
   2.元组内的元素不受数据类型限制，可以是数值类型，字符串，列表，元组，字典，集合等类型
   3.当定义一个只包含一个元素的元组时，必须在元素末尾加上逗号，否则python会将其视为该元素的数据类型本身，而不是一个元组
   nums1 = (1,)
"""
# tua = (False,3.5,"bingbing",[1,2],(1,2))
# print(tua,type(tua))
#
# nums = (1)  # 输出int
# nums1 = (1,)  # 输出元组
# print(nums,type(nums))
# print(nums1,type(nums1))

"""元组元素索引与切片（与字符串，列表读取类似）"""
# tua = (1,2,3,4,5)
# print(tua[2])  # 3
# print(tua[0])  # 1
# print(tua[-2])  # 4
# # print(tua[6])  # 报错。超出索引范围
#
# print(tua[1:4:2])  # 包前不包后

"""元组：可迭代对象
for i in tua
"""
'''元组常见操作：仅支持查询操作
in：检查一个元素是否存在于元组中，如果存在，返回Ture;否则，返回False
not in :检查一个元素是否存在于元组中，如果不存在，返回Ture;否则，返回False
index（）：查找元素所在索引位置，多个元素并存，取第一个元素的索引位置，未存在元素查询，报错
         index（value,start，stop） 包前不包后
count():统计元素出现次数
len(object):获取容器（列表，元组，字符串，字段，集合等）中元素的数量
即长度或大小。获取非容器类型（如整形，小数点等）长度，报错、
object:获取对象
'''
# tua = (1,2,3,4,5)
# print(1 in tua)  # True
# print(8 in tua)  # False
# print(8  not in tua)  # True
#
# print(tua.index(2))  # 1
#
# print(tua.count(2))  # 1

tua = (1,2,3,4,5)
str = "bingbing"
li  = [1,2,3,4,5]
print(len(tua))  # 5 元组长度
print(len(str))  # 8 字符串长度
print(len(li))   # 5 列表长度
print(len(1))   # 报错，非容器


