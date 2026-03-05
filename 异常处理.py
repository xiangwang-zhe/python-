"""
异常处理：try  excep
try :
尝试执行的代码块
expect 异常类型 as 变量
检测到异常要执行的代码块
else ：
没有检测到异常要执行的代码块
finally:
无论是否检测到异常都会执行的代码块

"""
# try:
#     mun = int(input("输入一个输："))
# except:
#     print("转换失败")
'''
except语句
   1.声明错误类型，ValueError,NameError
   2.多个类型，可以使用元组
   3.Exception:捕获程序中，任意非语法错误类型的异常（不报错）
   ，并允许我们获取异常的具体描述信息（获取错误类型）
   注意E大写，多个异常错误，只会捕获第一个异常信息
   except Exception as e:   
# 任意非语法异常，并将(异常对象)错误类型信息保存在变量e中
   '''
# try:
#     # mun = int(input("输入一个输："))
#     print(num)
# except (ValueError,NameError):    # 只捕获值错误，非数值问题报错
#     print("输入值有问题")

# try:
#     mun = int(input("输入一个输："))
#     print(num)
# except Exception as e:    # 任意非语法异常，并将(异常对象)错误类型信息保存在变量e中
#     print("异常具体描述信息",e)  # 获取异常的具体描述信息，以便进行进一步处理
# # 异常具体描述信息 invalid literal for int() with base 10: 'ghj'
# # 异常具体描述信息 name 'num' is not defined

'''else语句：代码块成功执行并没有引发任何异常时，
你希望执行的一些额外的代码，此时可以放入else语句块中
'''
# try:
#     num1 = int(input("输入一个输："))
# except Exception as e:
#     print("异常具体描述信息",e)
# else:
#     print("转换成功")
#     print(num1)

"""
finally语句：用于定义无论是否发生异常都要执行的代码块
它通常与Try和except语句配合使用，以确保即使在遇到错误时也能执行某些操作
如关闭文件，释放系统资源等
"""
# print('打开文件')
# try:
#     print(文件操作)
# except Exception as e:
#     print(e)
# else:
#     print("操作成功")
# finally:
#     print("关闭文件")

'''抛出自定义异常：程序主动抛出一个异常，用raise语句来实现
   raise语句：允许你指定要抛出的异常类型和可选的异常信息
raise Exception("密码长度不足8位，输入失败！~")
Exception: 密码长度不足8位，输入失败！~
'''
# 需求：用户输入密码，如果密码长度不足8位数，则系统主动抛出异常
def input_pwd():
    pwd = input("请输入你的密码：")
    if len(pwd) <= 8:
        raise Exception("密码长度不足8位，输入失败！~")
        print("密码少于8位数")
    else:
        print("密码输入成功")
    return pwd

# 已定义异常，将异常应用与程序
try:
    print(input_pwd())
except Exception as e:
    print(e)


