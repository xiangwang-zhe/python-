'''集合是一个无序的，不包含重复元素元素的数据结构。主要用于数学上的集合操作，如并集，交集，差集和对称差集等
语法格式 变量名 = {元素1，元素2，元素3，}
注：1.集合的元素被放置在一对花括号{}，各个元素之间使用逗号，进行分隔
   2.在python中花括号{}通常用于定义空字典，而空集合应该使用set()来定义
'''
# s = {1,2.3,4}
# print(s,type(s))  # {1, 2.3, 4} <class 'set'>
'''空字典{}与空集合set{}'''
# data = {}
# print(data,type(data))  # {} <class 'dict'>
# data2 = set()
# print(data2,type(data2))  # set() <class 'set'>
'''特点
1.无序
2.唯一
3.元素可哈希性（集合不可哈希），列表中不可哈希意味着对象是可变的
  可哈希：整数，浮点数，字符串，元组
'''
'''无序'''
# s = {'a','b','c','d','e'}  # {'a', 'b', 'c', 'd', 'e'}
# print(s)  # 每次输出的集合元素是无序的，随机排列
'''唯一'''
# s = {'a','b','c','d','b','a'}
# print(s)    # {'a', 'c', 'b', 'd'}

'''常见方法
1.添加元素
(1)add(element):向集合中添加元素。如果存在，不执行任何操作
set.add(element)
element:要添加元素（可哈希）
(2)update(iterable,*iterable):向集合中添加一个或多个元素，将可迭代对象中美的所有元素诼个添加到集合中
set.update(iterable,*iterable)
iterable:可迭代对象：列表，元组，集合等
*iterable(可选)：任意数量的可迭代对象。它们的元素将被诼一添加到集合中。但实际使用中，通常不会直接传递多个可迭代对象作为位置参数（即）
'''
"""set.add(element)"""
# s = {'a','b','c'}
# s.add('d')
# print(s)
'''set.update(iterable,*iterable)'''
# s = {'a','b','c'}
# s.update({'d','e'},(1,2,3))
# print(s)

'''删除元素
(1)remove(element):从集合中移除指定的元素。存在，移除；不存在，报错
set.remove(element)
（2）discard(element):从集合中移除指定元素。如果存在，移除，不存在。无反应
set.discard(element)
'''
'''set.remove(element)'''
# s = {'a','b','c'}
# # s.remove('d')  # 报错
# s.remove('b')  # {'c', 'a'}
# print(s)
'''set.discard'''
# s = {'a','b','c'}
# s.discard('b')  # {'c', 'a'}
# s.discard('d')  # 无反应
# print(s)

'''3.数学操作
交集
(1)使用&操作符：多个集合使用，返回一个新的集合，集合元素为共有元素（空集set（））
(2)使用intersection:用于多个集合交集
   set = set.intersection(iterable).intersection(iterable)
并集
(1)使用|操作符：多个集合使用，返回一个新集合，集合元素为所有元素（去除多余重复元素）
(2)使用union:用于多个集合并集
   set = set.union(iterable).union(iterable)
'''
'''&'''
# s1 = {1,2,3}
# s2 = {'a','b','c'}
# s3 = {1,'a','b','c'}
# # s4 = s1 & s2   # set()
# s5 = s1 & s3  # {1}
# print(s5)
''' set = set.intersection(iterable).intersection(iterable)'''
# s1 = {1,2,3}
# s2 = {1,'a','b','c'}
# s3 = {1,4,5,6}
# # s4 = s1.intersection(s2)  # {1}
# s5 = s1.intersection(s2,s3)
# s6 = s1.intersection(s2).intersection(s3)
# print(s6)

'''并集|'''
# s1 = {1,2,3}
# s2 = {'a','b','c'}
# s3 = {1,'a','b','c'}
# s4 = s1 | s2   # {'b', 1, 2, 3, 'c', 'a'}
# print(s4)
# s5 = s1 | s3 | s2 # {'b', 1, 2, 3, 'c', 'a'}
# print(s5)
'''set = set.union(iterable).union(iterable)'''
# s1 = {1,2,3}
# s2 = {'a','b','c'}
# s3 = {1,'a','b','c'}
# s4 = s1.union(s2)   # {'b', 1, 2, 3, 'a', 'c'}
# print(s4)
# s5 = s1.union(s2).union(s3)  # {1, 2, 3, 'b', 'a', 'c'}
# print(s5)

'''4.其他操作
(1)in:检查一个元素是否存在集合中，存在，Ture;不存在，False
(2)not in:检查一个元素是否存在集合中，不存在，Ture;存在，False
(3)len():集合长度（元素个数）
print(len(set))遍历集合
(4)for in :
'''
'''in'''
s = {1,2,3,'bing'}
print(1 in s)  # True

print(1 not in s)  # False

print(len(s))  # 4

for i in s:
    print(i, end=' \t')
