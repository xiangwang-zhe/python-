"""
封装、单继承、方法的重写、新式类写法
面对对象的三大特征：封装、继承、多态
封装：通过将对象的属性（即数据）和方法（即操作数据的函数）组合在一个单独的类中，
并对外隐藏这些内部实现细节，来达到特定的设计目标。这样的设计不仅提高代码的安全性，
还增强了代码的可维护性和可重复性。
继承：是实现代码重用的有效手段，它允许我们定义一个类（成为基类或父类）来包含
共同的属性和方法，然后创建这个类的一个或多个子类，子类可以继承父类的属性和方法，
也可以添加新的属性或附带（重写）父类的方法。这样，当多个类具有相似的属性和方法时，
我们可以通过及承诺来避免代码的重傅编写，使得代码更加简洁，易于维护。
多态：不同类型的对象可以调用相同的方法，但每个对象会根据其所属类的具体，来实现
细节来执行该方法，从而产生不同的结果。这种设计机制能够提高代码的灵活性和拓展性，
使得软件能够更容易地适应未来的变化和需求。
"""

'''
1.封装：将复杂的信息和流程隐藏在内部进行处理，对外仅提供简单、直观的操作接口，
让使用者通过简单的操作步骤即可实现所需的功能。
      类本质上就是一种封装，将属性和方法封装在内部；而实例化对象
则是通过调用这些封装好的成员（属性和方法）来执行具体功能

类中定义私有：对类进行封装
注：在python中，没有内置的私有装饰符用于直接声明属性或方法为私有。如果希望属性
或方法不被类外部直接访问，可以在其名称前添加双下划线（__）前缀
            self.__age = age            # 私有属性
修改私有属性
1.类中，定义公开方法：这是访问私有属性的推荐方式（访问）
# 定义公开方法访问私有属性
    def get_age(self)   :
        return self.__age

2.使用python的内部机制（改写）：
在python中，使用双下划线（__）开头的 属性名，实际上是一种命名约定，
旨在表明该属性私有的，不应在类外部访问。python解释器通过名称改写机制，自动将
这些属性名转换为 _类名__属性名 的形式
         print(p1._Person__age)
注：python并没有实现传统意义上的私有化，但它采用了一种命名约定，即在属性或
方法名前添加下划线（_）前缀，作为对内部成员私有性的标识，从而指导开发人员处理
需要隐藏或保护的数据和方法。


'''
'''未封装：修改类中属性'''
# class Person:
#     def __init__(self, name, age):  # 构造函数
#         self.name = name                 # 实例属性
#         self.age = age
#
#     def say_hello(self):
#         print(f"你好呀，我是{self.name}，今年{self.age}岁了")
# # 实例化对象
# p1 = Person("susu", 21)
# # 通过对象调用实例方法
# p1.say_hello()
# # 通过对象访问实例属性
# print(p1.name)
# # 修改实例属性
# p1.age = 20
# p1.say_hello()
# print(p1.age)
'''封装：私有属性'（ self.__age = age ）'''
# class Person:
#     def __init__(self, name, age):  # 构造函数
#         self.name = name            # 实例属性
#         self.__age = age            # 私有属性
#
#     def say_hello(self):
#         print(f"你好呀，我是{self.name}，今年{self.__age}岁了")
# # 实例化对象
# p1 = Person("bingbing", 18)
# # 尝试访问私有属性
# # print(p1.__age)  # 报错 AttributeError: 'Person' object has no attribute '__age'
'''修改封装'''
'''
1.定义公开方法访问私有属性
    def get_age(self)   :
        return self.__age
2.通过名称改写机制，访问私有属性：_类名__属姓名（不推荐）
     print(p1._Person__age)
'''
# class Person:
#     def __init__(self, name, age):   # 构建函数
#         self.name = name             # 实例属性
#         self.__age = age             # 私有属性
#     def say_hello(self):
#         print(f"你好呀。我是{self.name},今年{self.__age}岁了")
# # 定义公开方法访问私有属性
#     def get_age(self)   :
#         return self.__age
#
# # 实例化对象
# p1 = Person("bingbing", 18)
# # 尝试访问私有属性
# print(p1.get_age())
# '''改写私有属性'''
# # 通过名称改写机制，访问私有属性：_类名__属姓名（不推荐）
# print(p1._Person__age)


'''
2.单继承
继承：一种构建类之间关系的强大机制，它让类与类之间形成类似父子的层级结构。其中
子类默认会“继承”父类的所有非私有属性和方法。

作用：在编写类时，我们不必每次都从零开始。当发现新类与已存在的类之间存在合理的
继承机制，可以自然地实现代码的重用，避免重复编写相同的代码段，从而显著提升开发效率
语法格式
            class 类名（父类名）：
                    类的描述信息
                    类体
注：可以指定多个父类，父类名之间用逗号，分隔；若未指定父类，则默认继承自object类
（python中的顶级父类）

根据子类继承的父类数量分类：单继承和多继承
单继承：子类只从一个父类继承属性和方法。
多继承：子类可以从多个父类继承属性和方法。

单继承：一个子类继承父辈的所有非私有属性和方法，这是面向对象编程中最基本的继承形式，
简化了类的层次结构，使类的关系更加清晰，同时也促进了代码的重用。

"""
python中，创建子类对象，未创建父类对象，这个对象是子类与父类共用的吗
不是，这个对象不是子类与父类“共用”的。它是一个完全属于子类的独立对象
"""


'''
# class Person:
#     age = 18
#     def __init__(self, name):
#         self.name = name          # 实例属性
#     def greet(self):
#         print(f"你好呀，我是{self.name}")
# # 定义子类，继承自Person类（父类）
# class Student(Person):
#     pass
#
# # 通过类访问类属性
# # print(Student.age)
# # 实例化子类对象
# student = Student("bingbing")  # 子类继承父类__init__方法
# # 通过对象访问实例属性
# print(student.name)

'''
继承的传递性
python的继承具有传递性，这意味这如果类A继承自类B，而类B又继承自类C及其所有
祖先类中定义的非私有属性和方法。这确保了子类能够继承并使用所有父类及更上层
父类的非私有成员

'''
# class C:
#     c_var = "c类类属性"
#     def c_method(self):
#         print("这是c类的c_method方法")
#
# class B(C) :
#     b_var = "B类类属性"
#     def b_method(self):
#         print("这是b类的b_method方法")
#
# class A(B) :
#     a_var = "A类类属性"
#     def a_method(self):
#         print("这是a类的a_method方法")
#
# # 通过A类访问类属性
# print(A.a_var)
# print(A.b_var)
# print(A.c_var)
# # 实例化A类对象
# a = A()
# # 通过子类对象调用实例方法
# a.a_method()
# a.b_method()
# a.c_method()

"""
3.方法的重写：在python中，方法的重写是指子类定义了一个与父类中同名的方法
分类：
1.覆盖父类方法：当子类定义了一个与父类同名的方法时，子类的方法就会覆盖父类中
的方法。
2.对父类方法进行扩展：通过在子类中定义一个与父类同名的方法，并在该方法内部
首先调用父类的同名方法（以保留父类的行为），然后添加额外的逻辑来实现。

在python中，对父类方法进行扩展是一个常见的做法，它允许子类在继承父类方法的
基础上添加或修改功能。这通过在子类中定义一个与父类同名的方法，并在该方法内部
首先调用父类的同名方法（以保留父类的行为），然后添加额外的逻辑来实现。

子类调用父类的同名方法，实现方式通常有以下三种：
1.父类名.方法名(self)
Parent.show(self)
不推荐，一旦父类名改变，增加维护成本
2.super().方法名（）
super().show()
这是Python中一种非常常见且推荐的方式来调用父类中的方法。这种方式避免了直接
依赖具体的父类名，从而提高了代码的灵活性和可维护性。
3.super（子类名，self）.方法名（）
这是Python 2.x中调用父类的传统写法，而在Python 3.x 中虽然仍可使用，但
出于简洁性和代码可读性的考虑，通常采用更现代化的super().方法名（）形式，
后者在Python 3.x 中被优化以简化父类方法的调用

"""
''''''
# class Parent:
#     def show(self):
#         print("这是Parent类的show方法")
#
# class Child(Parent):
#     def show(self):
#         print("这是Child类的show方法")
#
# # 实例化子类对象
# Child = Child()
# # 通过子类对象调用
# Child.show()
'''1.父类名.方法名(self): Parent.show(self)'''
# class Parent:
#     def show(self):
#         print("这是Parent类的show方法")
#
# class Child(Parent):
#     def show(self):
#         # 调用父类的同名方法
#         # Parent.show(self)
#         # super().show()
#         super(Child,self).show()
#         # 额外的逻辑
#         print("这是Child类的show方法")
#
# # 实例化对象
# Child = Child()
# # 通过子类对象调用实例属性
# Child.show()

'''
4.新式类写法
在Python中，新式类是指任何直接或间接继承自 object 的类，这涵盖了直接继承
object 的类以及它们所有的子类，无论这些子类在继承链上的深度如何
写法一（推荐）：最新版（新式类） python 3.x
class 类名：
       类的描述信息
        类体
写法二（不推荐）：不必要混乱，与函数
class 类名（）：
       类的描述信息
        类体
写法三（推荐）：兼并python 2.x 与 python 3.x
class 类名（object）：
       类的描述信息
        类体
        
总结：在Python 3.x 版本中，object 是所有类的顶级父类（最基本类）。如果一个类在定义时，
没有显示地指定任何父类，它也会自动继承自 object,因此 python 3.x版本中的
所有类默认都是新式类

'''
'''写法一'''
class A:
   """A类"""
   pass
'''写法二'''
class B():
    """B类"""
    pass
'''写法三'''
class C(object):
    """B类"""
    pass

'''
封装：将类的属性定义为私人数据
self.__age = age            # 私有属性
'''
