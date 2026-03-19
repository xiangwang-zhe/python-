"""多继承，多态，静态方法，类方法"""
from ftplib import parse150

'''
多继承：允许子类同时继承多个父类，从而获取并访问这些父类的所有非私有属性和方法
class Child(ParentA, ParentB):
pass

1.2 不同父类间存在同名方法(有调用顺序：子类>A父类>B父类)
注：当不同父类之间存在同名属性或方法时，应当尽量避免使用多继承

1.3 方法搜索顺序
python中内置属性__mro__可以查看类的方法搜索顺序，这有助于我们理解并确定子类
在调用方法时，python将按照何种顺序查找并调用方法。
语法：   类名.__mro__

注：在多继承中，当存在同名方法时，Python将严格依据__mro__定义的顺序，从左至右
遍历及其所有基类的搜索方法。如果在当前类或任一类中找到了对应的方法，python就会
立即执行该方法，并停止进一步的搜索。如果遍历完整个__mro__元组，包括最基础的
object 类，都没有找到对应的方法，那么Python会抛出一个AttributetError异常。
明确指出该方法未被定义。

'''
# class ParentA:
#     a_var = "父类A类属性"
#     def a_method(self):
#         print("这是父类A类的方法")
# class ParentB:
#     b_var = "父类B类属性"
#     def b_method(self):
#         print("这是父类B类的方法")
#
# class Child(ParentA, ParentB):
#     pass
# # 访问父类类属性
# print(Child.a_var)
# print(Child.b_var)
# # 访问父类实例方法
# Child = Child()
# Child.a_method()
# Child.b_method()
'''不同父类间存在同名方法(有调用顺序：子类>A父类>B父类)'''
# class ParentA:
#     a_var = "父类A类属性"
#     def method(self):
#         print("这是父类A类的方法")
# class ParentB:
#     b_var = "父类B类属性"
#     def method(self):
#         print("这是父类B类的方法")
# class Child(ParentA, ParentB):
#     def method(self):
#         print("这是子类的方法")
#
# # 访问父类实例方法
# Child = Child()
# Child.method()
"""查看子类调用顺序的方法：Child.__mro__"""
# class ParentA:
#     pass
#     # a_var = "父类A类属性"
#     # def method(self):
#     #     print("这是父类A类的方法")
# class ParentB:
#     pass
#     # b_var = "父类B类属性"
#     # def method(self):
#     #     print("这是父类B类的方法")
# # 定义Child类，同时继承自ParentB
# class Child(ParentA, ParentB):
#     pass
#     # def method(self):
#     #     print("这是子类的方法")
#
# # 查看子类方法搜索顺序
# print(Child.__mro__)
# # 实例化子类对象
# Child = Child()
# # 通过子类对象调用实例方法
# # Child.method()
# # 通过子类对象调用__str__
# print(Child.__str__())  # 调用object类的__str__方法

"""2.多态"""
'''
多态：同一种行为在不同类型的对象上展现出多样化的表现形式。

2.2 前提
1.继承
2.方法的重写


'''
# # 定义Animal类
# class Animal:
#     """动物类"""
#     def speak(self):
#         print("动物说话")
#
# #定义Dog类，继承自Animal类
# class Dog(Animal):
#     def speak(self):
#         """狗类"""
#         print("汪汪")
#
# #定义Cat类，继承自Animal类
# class Cat(Animal):
#     def speak(self):
#         """猫类"""
#         print("喵喵")
#
# # 定义一个统一的接口，接受一个Animal类型的参数（或其子类对象），
# #  并调用该对象的speak方法，
''' 接口(函数)，参数应为接口，所面向的类。这样在调用接口（函数），输入参数，
可根据所提供的类，查找它以及它所包含的子类，并执行
'''
# def animal_speak(animal):
#     """同一的接口，用于调用传入对象的speak方法"""
#     animal.speak()
# # 实例化对象
# dog = Dog()
# cat = Cat()
# # 调用接口，传入不同的对象，产生不同的执行结果
# # 由于多态性，animal_speak能够识别传入对象的实际类型，并调用相应类型的speak方法
# animal_speak(dog)  # animal = dog  ==> animal.speak() = dog.speak
# animal_speak(cat)
#
# dog.speak()
# cat.speak()

# # 需求：利用多态的思想，编写程序，模拟“主人（Master）”喂养“宠物（pet）的场景”
# # 定义宠物类
# class Pet:
#     """宠物类，父类"""
#     def eat(self):
#         print("宠物吃东西")
#
# # 定义狗类，继承父类
# class Dog(Pet):
#     def eat(self):
#         print("狗吃东西")
#
# # 定义猫类，继承父类
# class Cat(Pet):
#     def eat(self):
#         print("猫吃东西")
#
# # 定义猪类，继承父类
# class Pig(Pet):
#     def eat(self):
#         print("猪吃东西")
#
#
# # 定义主人类
# class Master:
#     """主人类，负责喂养宠物"""
#     def feed(self, pet):
#        pet.eat()
#
# # 实例化对象
# ma = Master()
# dog = Dog()
# cat = Cat()
# pig = Pig()
#
# # 主人喂养不同的宠物
# ma.feed(dog)
# ma.feed(cat)
# ma.feed(pig)

"""3.静态方法"""
'''
静态方法：使用@staticmethod修饰的方法。静态方法在定义时不接受也不应包含类
对象（cls）或实例对象（self）作为参数，因为这些方法不依赖于类或其实例的状态。

定义格式：
@staticmethod
def 方法名（形参）：
 方法体
 注：使用时，形参没有限制
 
应用场景
当方法既不需要访问或修改实例对象的状态（如实例属性或实例方法），也不需要直接引
用类本身（如类属性、类方法或实例化对象）时，可以考虑将该方法定义为静态方法。
这样做有助于提高代码的清晰性，同时避免了不必要的参数传递。

特点：
（1）无默认参数：静态方法没有 self（实例）或 cls（类）参数。
它就像一个普通的函数，只是被放在了类的命名空间里。
（2）不能访问类/实例数据：因为它没有 self 或 cls，所以它无法直接访问实例属性或类属性。
(3)直接通过类调用：你不需要创建类的实例就可以直接通过类名调用静态方法。

'''
# # 需求1：在Person类中定义一个无参的静态方法。
# class Person:
#     """人类"""
#     @staticmethod
#     def study():          # 静态方法（无参）
#         print("人类爱学习")
#
# # 调用无参静态的方法
# Person.study()
# # 实例化对象               # 直接通过类名调用
# p1 = Person()
# print(p1.study())         # 通过对象调用
#
# # 需求2：在 Person 类中定义一个携带参数的静态方法
# class Person:
#     """人类"""
#     @staticmethod
#     def study():          # 静态方法（无参）
#         print("人类爱学习")
#     @staticmethod
#     def greet(name):          # 静态方法（无参）
#         print(f"你好啊，{name}")
#
# # 调用无参的静态方法
# Person.study()
# # 实例化对象               # 直接通过类名调用
# p1 = Person()
# p1.study()               # 通过对象调用
#
# # 调用带参的静态方法
# Person.greet("huohua")    # 直接通过类名调用，并传递参数
#
# p1.greet("shuihua")       # 通过对象调用

"""4.类方法"""
'''
类方法：使用@classmethod修饰的方法。类方法至少接受一个参数，这个参数按照惯例
被命名为cls,它代表了类本身，使得类方法能够执行与类本身紧密关联的操作，而不需要
的实例。

定义格式：
@classmethod
def 方法名（cls.形参）：
    方法体
    
注：python中，当定义一个类方法，无论是通过类本身还是通过该类的实例（对象）
来调用这个方法，python解释器都会自动将类本身作为第一参数传递给这个方法。
  
应用场景 
类方法一般和类属性配合使用，当方法中需要使用类（如访问类属性，调用其他类方法
或实例化对象）时，可以考虑将该方法定义为类方法。
'''
# # 需求：在Person类中定义一个类方法
# class Person:
#     """人类"""
#     @classmethod
#     def sleep(cls):         # 类方法
#         print("cls",cls)    # cls代表类本身
#         print("人类睡觉~")
#
# # 通过类调用
# Person.sleep()        # 直接通过类名调用
# print(Person)
#
# # 通过对象调用
# p1 = Person()
# p1.sleep()            # 也可以通过对象调用

class Person:
    """人类"""
    age = 18           # 类属性
    @classmethod
    def get_age(cls):
        # # 方法中访问类属性
        # print("年龄",Person.age)  # 一般类名变更，此处也需要修改
        print("年龄",cls.age)       #  有助于提高代码的可维护性（推荐）
# # 实例化对象
# p1 = Person()
# p1.get_age()
# 直接通过类调用
Person.get_age()



