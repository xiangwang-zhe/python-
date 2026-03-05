'''列表 list[元素，元素，...,元素]
元素：数值类型，字符串，列表，元组，字典，集合等（不受类型限制）
列表索引（字符串索引）  li[0],li[-1]
 列表切片（字符串切片）  li[start:stop:step） step：正负值，切片方向
列表可迭代 for ... in  li
'''
#
"""索引"""
# print(li[0])  # 1   从左往右
# #print(li[4])  #  报错  超过索引范围
# print(li[-1])  # d  从右往左
"""切片"""
# print(li[0:3:1])  # [1, 'b', 3] 包前不包后
# print(li[-1:-4:-1])  # ['d', 3, 'b']
# print(li[1:3:2])  # ['b']

"""列表可迭代对象"""
# for i in li:
#     print(i)

"""1.添加元素
（1）append（object）：在列尾添加元素
     li.append(object)
（2）extend(iterable):将一个可得迭代对象（列表，元组，字符串等）的所有元素诼一添加到列尾的尾部
      li.extend(iterable)
（3）insert(index,object):在列表的指定位置插入一个新的元素
      list.insert(index,object)
      （插入索引位置，原索引位置元素向后）
      超出索引位置范围，默认在末尾添加元素
index:元素将要被插入的索引位置
object:要插入到列表中的元素，可以任意数据类型
"""
'''append（object）：在列尾添加元素'''
# li = [1, 2, 3]
# li.append(4)  # [1, 2, 3, 4]
# li.append("abc")  # [1, 2, 3, 4, 'abc']
# print(li)

'''extend(iterable):将一个可得迭代对象（列表，元组，字符串等）的所有元素诼一添加到列尾的尾部'''
# li = [1, 2, 3]
# li.extend("456")  # [1, 2, 3, '4', '5', '6']
# print(li)

'''insert(index,object):在列表的指定位置插入一个新的元素'''
# li = [1,2,3]
# li.insert(1,"d")  # [1, 'd', 2, 3]    （插入索引位置，原索引位置元素向后）
# li.insert(5,"b")  # [1, 'd', 2, 3, 'b'] 超出索引位置范围，默认在末尾添加元素
# print(li)

'''2.修改元素:通过指定元素的索引来修改列表中的元素（直接替换）
li[index] = object
index：要修改的元素的索引位置
value: 要赋予指定索引位置的新值，任意类型
  '''
# li = [1,2,3]
# li[1] = 5
# print(li)

'''3.查找元素（字符串查询：str.index（），str.find(),str.count()）
 (1)in:检查一个元素是否属于列表（整体）元素。结果ture,false
       整体元素判断
 (2)not in：检查一个元素是否属于列表（整体）元素。结果ture,false
        整体元素判断
 (3)index(value,start,stop):查找列表中某个元素第一次出现的索引位置，如不存在，报错
 value:查找元素的值
 start(可选):开始查找的索引。默认为0
 stop(可选)：停止查找的索引，默认为列表的长度，即列表的末尾。（包前不包后,）
 (4)count(value):统计某个元素在列表中出现的次数。如果不存在，返回0
 value:统计出现次数的元素
 '''
'''in'''
# name = ["bingbing","susu","maiyi"]
# print("xiaohuan" in name)  # False
# print("bing" in name)  # False

'''not in'''
# name = ["bingbing","susu","maiyi"]
# print("xiaohuan" not in name)  # Ture

'''index(value,start,stop)'''
# li = [1,2,3,2]
# print(li.index(2))  # 只指引出元素第一次索引的位置
# print(li.index(2,2,3))  # 包前不包后，报错

'''count(value,start,stop)'''
# li = [1,2,3,2]
# # print(li.count(2))  # 2
# print(li.index(5))  # 报错

'''4.删除元素
(1)del: 根据索引删除列表中的元素，如果尝试删除一个不存在的索引对应的元素，则报错
      del.list[]
(2)remove:移除列表中第一个匹配指定值的元素，若不存在，则报错
list.remove(value) 
'''
'''del'''
# li = [1,2,3,2]
# # del li[2]  # [1, 2, 2] 删除索引位置2的元素
# del li[4]   # 报错 删除索引范围之外
# print(li)

'''remove'''
# li = [1,2,3,2]
# # li.remove(2)  # [1, 3, 2]
# li.remove(4)   # 报错 移除不存在元素
# print(li)

"""5.排序
（1）sort(key,reverse)：对列表中的元素进行排序 
参数默认：即key=None,reverse=False
key(可选)：接受一个函数作为参数，该函数会在每一个元素上调用，其返回值将作为排序的依据，如果未提供，则直接比较元素本身。
reverse(可选)：接受一个布尔值，如果设置为Ture,则列表将以降序排序；如果设置为False或未提供，则列表将以升序排序
（2）reverse（）：元素位置颠倒
"""
'''sort()'''
# li = [4,5,6,8,2,3,1]
# li.sort()  # [1, 2, 3, 4, 5, 6, 8] key=none,reverse=false
# print(li)

'''reverse()'''
# li = [4,5,6,8,2,3,1]
# li.reverse()  # [1, 3, 2, 8, 6, 5, 4]
# print(li)

'''6.列表推导式
从一个已存在的列表，以某一种方式，生产新列表
(1)[expression for item in iterable]
(从iterable中取出元素放入i中，再将每次i值放入expression)
expression:表达式，作为生产列表中的新元素
item:iterable中的当前元素
iterable:可迭代对象，如列表，元组，字符串，集合等 
(2)带有条件的列表推导式：加入条件，过滤出满足条件的元素
[expression for item in iterable if condition]
(从iterable中取出元素，若满足condtion,则放入i中，再将每次i值放入expression)
conditon:布尔表达式，用于指定哪些元素应该被包含在结果列表中
'''
'''[expression for item in iterable]
    生成一个列表，保存数字1-10.两种方法'''
# li = []
# for i in range(1,11):
#     li.append(i)
# print(li)
#
# li2 = [i for i in range(1,11)]
# print(li2)

'''[expression for item in iterable]
需求：生成一个列表，保存列表[11,22,33,44,55,66]中所有元素乘以5的结果'''
# i = [11,22,33,44,55,66]
# i2 = []
# for i in i:
#     i2.append(i*5)
# print(i2)
#
# i2 = [i*5 for i in range(1,11)]

'''[expression for item in iterable if condition]
需求：生成一个列表，保存列表[11,22,33,44,55,66]中所有偶数
'''
# li1 = [11,22,33,44,55,66]
# li2 = []
# for i in li1:
#     if i % 2 == 0:
#         li2.append(i)
#     else:
#         continue
# print(li2)
#
# li1 = [11, 22, 33, 44, 55, 66]
# li2 = [i for i in li1 if i % 2 ==0]
# print(li2)

'''7.镶嵌列表：一个列表中包含其他列表作为元素
访问镶嵌列表元素
'''
li = [1,2,[3,4,5]]
# 如何访问
print(li[1])  # 2 第一列表第2序列元素
print(li[2][1])  # 4 6第一列表的第3序列元素（列表）中的序列1的元素
