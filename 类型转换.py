"""数据转换
(1)int():将值（其他数据类型：浮点数，布尔型，字符串，+-区别）转换为整性，无法识别，报错
print(int())
“+”“-“作为正负号可以。加减符不可以
浮点数直接去调小数点1.2-1
(2）float() :将值转换为浮点型（整数，布尔型，字符串），无法识别，报错
print（float()）
(3)bool():将值转换为布尔型，评估（一些值为真，返True，一些值为假，返False）
假：false，none，任何数值类型中的零（如0,0.0，0j）,空序列[],空集 set（）
(4)str（）：将值转换为字符串型，几乎可以将任何数据类型转换为字符串
(5)eval（）：执行字符串表达式（不是语句），并返回表达式的值
    result = eval（）
    print(result)
(6)list():将值转换为列表数据,是一个内置函数，用于将可迭代对象转换为列表（list）
字符串，元组（tup）,字典（dict,问题只接收键名），集合（set）
(7)tuple():将值转换为元组数据，方法同list()
(8)dict():将值转换为字典型数据。一般不能直接将其他数据类型转换为字典，
但可使用dict（）结合其他python特定类型到字典的转换。直接的类型转换，是指将一个结构化的数据类型
（如包含键值对信息的类型）转换为字典
关键字参数：mydict = dict(name = "bingbing", age = 18, sex ="女")
转换类型（list[],tuple(),set{}）其元素为元组，且每个元组是一对键值
set = (("a",1),("b",2),("c",3))
(9)set():将值转换为集合型数据 ：将可迭代对象
（如字符串（str）,列表(list)，元组（tuple）,字典(dict)，range对象等）
转换为集合


"""
'''1.print(int())'''
# print(int(1.2))  # 1  浮点数
# print(int(True))  # 1  布尔型
# print(int(False))  # 0
# print(int("123"))   # 123  字符串
# print(int(-1.2))  #-1  正负号
# print(int(1-2))  # 无反应  整数加减符号
# print(int("1-2"))  #报错  字符串中加减
'''2.print(float())'''
# print(float(1))  # 1.0  整数
# print(float(True)) # 1.0 布尔型
# print(float(False))  # 0.0
# print(float("123"))  # 123.0 字符型
# # print(float(c))    # 报错
'''3.print(bool())'''
# print(bool(2))  # True  整数
# print(bool(0))  # False
# print(bool(0.0))  # False 小数（float）
# print(bool(''))  # False  字符串
# print(bool(0j))  # False
# print(bool([]))  # False 空列表
# print(bool(set()))  # False 空集合
# print(bool({0,}))  # false
# print(type(()))  # 元组（tua）
# print(bool(()))  # 空元组
# print(bool(set())  #空集合 （set）
# print(type(set()))
'''4.print(str())'''
# print(str(123),type(str(123)))  # 整数
# print(str(1.2),type(str(1.2)))  # float
# print(str(True),type(str(True)))  # bool
# print(str(()),type(str(())))  # tup
# print(str({}),type(str({})))  # info（dict）
# print(str([]),type(str([])))  # list
# print(str(set()),type(str(set())))
'''5.eval():字符串表达式'''
# result = eval("2+1")
# print("1"+"2")  # 12
# print(result)  # 3

# result = eval('{"name":"bingbing","age":18}["age"]')
# print(result   # 18  列出字典，根据键名查找键值

'''6.list()'''
# st = "hello"
# print(list(st))  # 字符串
# tup = (1,2,3,4,5)
# print(list(tup))  # 元组
# dict = {"name":'xiao',"age":'hua'}
# print(list(dict))  # 字典，只转换出键名
# dict = {"name":'xiao',"age":'hua'}
# keys = dict.keys()  # 取键名
# print(list(keys))
# values = dict.values()  # 取键值
# print(list(values))
# items = dict.items()
# print(list(items))  # 取键值对
# set = {2,3,5}
# print(list(set))  # 集合
# list(range(1,6))  # rang
# print(list(range(1,6)))  #

'''8.dict()'''
'''使用关键字参数'''
# mydict = dict(name = "bingbing", age = 18, sex ="女")
# print(mydict)  # {'name': 'bingbing', 'age': 18, 'sex': '女'}
# '''list转字典：list元素为元组，且每个元组是一对键值'''
# li = [("a",1),("b",2),("c",3)]
# li_dict = dict(li)
# print(li_dict)
'''tuple转字典：tuple元素为元组，且每个元组是一对键值'''
# tup = (("a",1),("b",2),("c",3))
# tup_dict = dict(tup)
# print(tup_dict)
'''set转字典：set元素为元组，且每个元组是一对键值'''
# set = (("a",1),("b",2),("c",3))
# set_dict = dict(tup)
# print(set_dict)

'''set()'''
st = 'ab'
print(set(st))  # {'a', 'b'}  str转set
li = ['a','b','c']
print(set(li))   #{'c', 'a', 'b'} list转set
tup= ('a','b','c')
print(set(tup))   # {'a', 'c', 'b'} tuple转set
dict = {"a":1, "b":2, "c":3}
print(dict.keys())  # 取键名 dict转set
# dict_keys(['a', 'b', 'c'])
print(dict.values())   #取键值
# dict_values([1, 2, 3])
print(dict.items())   #取键值对
#dict_items([('a', 1), ('b', 2), ('c', 3)])
range = range(1,5)  # ranges转set
print(set(range))  # {1, 2, 3, 4}
