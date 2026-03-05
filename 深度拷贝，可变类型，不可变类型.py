"""赋值：本质上是创建一个新的引用对象（新名称），而不是创建一个副本
同一对象（操作共享），判断是否是同一对象：比较两者是否属于同一地址
"""
# li1 = [1, 2,[3, 4]]
# li2 = li1
# print("li1",li1)
# print("li2",li2)
# print(id(li1) == id(li2))  # True
#
# li1.append(5)
# print("li1",li1)
# print("li2",li2)
#
# li2.append(6)
# print("li1",li1)
# print("li2",li2)

'''深浅拷贝 :新与旧，是否相随而变
生成的新对象与原对象的区别程度：内容相同，内存地址不同（共享）
浅（第一层不同，镶嵌相同（随变而变）） 深：所有都不同（随变不变）
 # 首先导入copy模块：import copy  
不同于赋值，copy创建新对象，内存地址是不同的（改变对象，新对象不改变）
     print(id(li)==id(li2))  # False
含有嵌套元素，嵌套元素的内存地址是相同的（改变对象，新对象改变）
     print(id(li[2])==id(li2[2]))  # True
浅拷贝：只拷贝原始对象的第一层数据。如果原始对象包含嵌套的可变对象（如列表，字典等）
浅拷贝后的新对象将不会复制这些嵌套对象，而仅仅复制它们的引用（即内存地址）
新对象你和原始对象会共享这些嵌套层的可变对象 
深拷贝：创建一个新对象，并且递归地复制对象中包含的对象，直到所有对象都被复制 
原对象和深拷贝后的对象在内存中是完全独立的，对深拷贝对象的修改不会影响到原对象
'''
'''浅拷贝（copy.copy）'''
import copy
# li = [1,2,[3,4]]
# li2 = copy.copy(li)
# print("li",li)
# print("li2",li2)
# print(id(li)==id(li2))  # False 第一层元素内存地址不相同， 不共享
# li.append(5)
# print("li",li)
# print("li2",li2)
# print(id(li[2])==id(li2[2]))  # True  镶嵌元素内存地址相同，共享
# li[2].append(6)
# print("li",li)
# print("li2",li2)
'''深拷贝（copy.deepcopy）'''
# li = [1,2,[3,4]]
# li2 = copy.deepcopy(li)
# print(id(li) == id(li2))  # False 第一层元素内存不同，不共享
# print(id(li[2])==id(li2[2]))   # False 嵌套元素内存不同，不共享
# li.append(5)   # 第一层元素
# li[2].append(6)  # 嵌套元素
# print(li)
# print(li2)


"""可变数据与不可变数据的区别：修改后内存地址是否改变"""
'''
可变类型：存储空间保存的数据允许被修改，修改后内存地址不变
list,dict,set

'''
'''li[index] = value'''
# li = [1,2,3]
# print("修改前的内存地址：",id(li))
# li[1] = 5
# print("修改后的内存地址：",id(li))
'''dic[keys] = value'''
# dic = {'a':1,'b':2}
# print("修改前的内存地址：",dic,id(dic))
# dic['c'] = 5
# print("修改后的内存地址：",dic,id(dic))
'''set.remove(element)'''
# s = {1, 2, 3}
# print("修改前的内存地址：",s,id(s))
# s.remove(2)
# print("修改前的内存地址：",s,id(s))

'''不可变类型：存储空间保存的数据不允许被修改，修改后内存地址不同
数值类型：整数int,浮点型float，布尔型bool.复数型complex

'''
# n = 10
# print("修改前的内存地址：",n,id(n))
# n = 15
# print("修改前的内存地址：",n,id(n))
'''str.replace(old, new)'''
# str = 'huohua'
# print("修改前的内存地址：",str,id(str))
# str = str.replace('huohua','shuihua')
# print("修改前的内存地址：",str,id(str))
'''元组不可修改，直接赋值'''
tup = ('huohua')
print("修改前的内存地址：",tup,id(tup))
tup = ("shuihua")
print("修改前的内存地址：",tup,id(tup))



