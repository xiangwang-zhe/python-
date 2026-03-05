"""函数：一段功能代码，可反复调用"""
from itertools import count

'''1.定义：
def 函数名（）：函数描述信息
    函数体
    2.调用函数前，函数必须被定义，否则，报错 (代码执行规则：自上而下)
    '''
# #需求：小孩0-3，重复讲述故事3次；3-5岁，只讲一次
# age = int(input("请输入你的年龄："))
# if 3 >= age >= 0:
#     for i in range(3):
#         print(i)
# elif 6 >= age >= 3:
#     print(1)

# def say_story():  # 定义函数
#     for i in range(3):
#         print(i)
# say_story()  # 调用函数
# '''优化'''
# age = int(input("请输入你的年龄："))
# if 3 >= age >= 0:
#     say_story()
# elif 6 >= age >= 3:
#     print(1)

'''返回值（return）：函数执行完成后，向调用者提供的最终处理结果或数据
(1)向调用者提供最终处理结果或数据，以便进行后续的操作或逻辑判断
注：
   1.函数中没有使用return语句显式地返回一个值，
或者return语句后面没有跟任何值，那么函数结束时隐式地返回None作为结果
   2.如果函数有一个返回值，那么它会执行到return语句时将该值返回给调用者（定义变量接受）
   返回值类型不变
   3.当函数需要返回多个值时，python允许你以元组（tuple）的从事返回这些值
'''
# def add_numbers():  # 将两个数相加并返回结果
#     a = float(input("请输入第一个数"))
#     b = float(input("请输入第二个数"))
#     return a + b
# result = add_numbers()  # 调用函数需返回值result用于接受结果
# print(result)
"""检查返回值"""
# if result > 7:
#     print("结果大于7")
# elif result < 7:
#     print("结果小于7")
'''后续处理'''
# total = result + 1
# print('输出总额', total)

# def fun():
#     return 123  # return表示立刻停止，并返回值，
#     print(456)  # return后 不执行
# print(fun())
"""多个返回值，以元组（tuple）返回"""
# def fun():
#     return 1,2,3  # return返回多个值以元组的形式 (1, 2, 3)
# print(fun())

'''参数'''
'''形参&实参
形参：函数定义时指定的参数。他们代表函数期望接受的值的占位符。在函数被调用之前，形参并不实际存储任何值。
     形参只在函数被调用时才会被赋予具体值，这些值来自于函数调用时提供的实参
     def add(a, b):   # a,b形参
实参：调用函数时传递给函数的实际值，这些值被赋值给形参，以便函数能够使用
     它们来执行其定义的操作
     add(1, 2)  # 将实参传递给形参
     '''
'''函数参数
1.必备参数（位置参数）：传递参数的顺序和个数必须与函数定义时指定的参数顺序和个数一致
2.缺省参数（默认参数）：在函数定义时，可以为参数指定默认值。
              若调用时没有提供该参数值，则使用默认值
              默认参数要放在非默认参数之前，否则报错
              def greet(name = "bingbing"): {= "bingbing"}为默认值
3.可变参数（*args）：可以允许函数接受任意数量的位置参数。这些参数会被收集到一个名为args的元组中
4.关键字参数：使用**kwargs可以允许接受任意数量的关键字参数。
这些参数会被收集到一个名为kwargs的字典中
（同样，你可以使用任何变量名，但kwargs是惯例）
greet(name="bingbing")  # {'name': 'bingbing'} 你好 键值对

'''
# 定义函数实现加法运算
# def add_fun():
#     m = int(input("请输入第一个数"))
#     n = int(input("请输入第二个数"))
#     s = m + n
#     print(s)
#
# add_fun()

# def add():
#     a = 1
#     b = 2
#     return a + b
#
# result = add()
# print(result)

# def add(a, b):   # a,b形参
#         return a + b
#
# result = add(1, 2)  # 将实参传递给形参
# print(result)

# def greet(name, greeting):
#     print(f' {name},{greeting}')
# greet("shui","huo")

# def greet(name = "bingbing"):
#     print(f"{name}","你好呀！")
# greet()  # bingbing 你好呀！
# greet("susu")  # susu 你好呀！
'''形参*agrs:默认为可加任何数量的形参'''
# def greet(*agrs):
#     print(f"{agrs}","你好呀！")
# greet()
# greet(1,2,3)  # (1, 2, 3) 你好呀！
'''**kwargs:任意关键字'''
# def greet(**kwargs):
#     print(f"{kwargs}","你好")
#
# greet()
# #greet(name)  # 报错
# greet(name="bingbing")  # {'name': 'bingbing'} 你好 键值对

# def register_users(username,age, **kwargs):
#     print(F"用户名：{username},年龄：{age}")
#     for key in kwargs.keys():  # 这些参数会被收集到一个名为kwargs的字典中
#         print(f"额外信息：{key}={kwargs[key]}")
# register_users("bingbing" ,30)
# # 调用函数，同时提供可选项
# register_users("bingbing",30,email="<EMAIL>")

'''变量作用域
1.含义：程序代码能够访问该变量的区域，也就是变量生效的范围
2.分类：局部变量和全局变量
局部变量：在函数内部定义的变量，函数外，不可用
全局变量：在函数外部定义的变量，在整个程序执行过程中都是可访问的
局部变量与全局变量相同，局部变量会覆盖全局变量（只在局域作用域内，除此，全局变量不变）
globe&nonlocal()
globe:关键字用于函数内部，声明全局变量 global count    #  声明count是全局变量
用于函数内部，定义全局变量，
nonlocal:关键字用于在内层函数中引用并可能修改外层函数作用域中的局部变量，
        同时确保这个变量不是在当前函数内部新创建的局部变量，也不是全局变量
声明变量是外层函数的局部变量，修改后作用于之后的整个局部变量，不作用与全局范围
'''
# def func():
#     x = '局部变量'
#     print("func:", x)
#
# func()           # func: 局部变量
# print("外部",x)   #NameError: name 'x' is not defined

'''局部变量与全局变量相同，局部变量会覆盖全局变量（只在局域作用域内，除此，全局变量不变）'''
# x = "全局变量"
# def func():
#     print("func:",x)
#
# func()           # func: 全局变量
# print("外部：",x) # 外部： 全局变量

'''global&nonlocal'''
# count = 1
# def increment():
#     global count    #  声明count是全局变量
#     count += 1      # 修改全局变量的值 count
#
# increment()
# print("外部：",count)  # 外部： 2

# def increment():
#     global count
#     count = 1
# increment()
# print("count：",count)
'''声明多个全局变量（在global后，逗号隔开）'''
# def incream():
#     global num,count
#     num = 1
#     count = 1
#
# incream()
# print(num, count)

'''nonlocal '''
def outer():               # 外层函数
    a = 10
    print("outer1", a)
    def inner():           # 内层函数
        nonlocal a         # 声明a是外层函数的局部变量
        a = 20
        print("inner", a)
    inner()                # 调用内层函数
    print("outer2", a)
'''调用内部函数，同级调用'''
outer()                    # 只调用外层函数





