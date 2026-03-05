"""内置模块：一般导入模块，会放在文件最开头
python如copy，random(随机),time,os等，这些模版可以直接使用
"""
# # 导入随机模块
# import random
# # 生成一个1-3（包括1和3）之间的随机整数
# num = random.randint(1,3)
# print(num)

'''第三方模块：不是python官方标准库的一部分
使用之前，需要下载和安装他们。
python提供一个名为pip的宝宝管理工具，用于下载和安装第三方模块
在命令行或终端中，使用pip安装第三方模块的命令如下：
     pip install 模块名 
示例：pip install requests
'''
import requests

'''自定义模块：自定义的一些模块
创建时，应确保命名遵循python的表示符规定和变量的命名规范
    避免与python的内置模块以及已安装的第三方模块命名发生冲突，
    以防止模块功能出现异常或无法使用
'''

'''
导入模块（两种方式）
第一种：import 模块名   # test.func()
第二种：from 模板名 import 功能名  从模块中导入指定的部分 # func()
'''

'''
1.import模块名（as 别名）：导入模块所有内容
新建.py文件作为模块，若使用过程中，别名较长可以使用as关键字为其设置别名
可调用模板中的任意信息    print(t.name)

'''
# import test
# test.func()

# import test as t
# t.func()
# print(t.name)

'''
2. from 模板名 import 功能名：从模块中导入指定功能
注：使用这种方式导入后，无需添加“模块名”作为前缀，
   直接通过具体的变量名，函数名或类名等即可直接访问
   func()
导入模块的所有内容：通过使用from...import * 语法来实现
注：语句导入时，确保不同模块间的内容不可重名，否则会产生冲突
'''
# 需求：从test模版中导入func函数，并执行该函数
# from test import func
# func()
# # print(name)  # 报错，并没有导入变量，指导入了函数
#
# from test import *  # 从test文件中导入所有信息
# func()
# print(name)
'''name，test与本文件重名，报错'''
# from test import *
# name = "bingbing"
# print（name）
'''重名，区分，最好用import'''
# import test
# name = "bingbing"
# print(test.name)
''''''

'''以主程序的形式执行
如果一个模块式直接被运行的，而不是被导入到其他程序中，那么_name_变量的值会被设置为“_main_”,.
若这个模块是被导入到其他模块中执行的，那么_name_变量的值就会被设置为该模块的模块名
示例：test文件run,__name__的值为__main__,而在
主文件（此文件）中，__name__的值为文件名（模块名）test
'''
# # 需求：导入test模块
# import test
"测试代码，可加条件限制其在主文件或模块的执行,详见test(if)"


'''包（package）：命名符合规范
为了解决模块名重复的问题，引入包（package）的概念
包是一个分层次的目录结构，用于将一组功能相近的模块组织在一起，这样不仅有助于规范
代码结构，还能有效避免模块名之间的冲突。
简单来说，包就是一个特殊的“文件夹”，用于组织和管理相关的代码
'''
'''
导入包的方式（__init__文件会自动执行，作为包初始的一个环节）
1.import 包名（.模块名）:导包
# 导入名为pack01的包
 import pack01 
# 导入pack01.test01的模块
 import pack01.test01
# 输出test01模块中name变量的值 
 import pack01.test01
'''
# # 需求：导入名为pack01的包
# import pack01
# # 导入pack01.test01的模块
# import pack01.test01
# # 使用功能：包名.模块名.功能名
# # 输出test01模块中name变量的值
# print(pack01.test01.name)

# # 需求：导入 pack01 包下test01 的模块，并输出test01模块中 name 变量的值
# # 使用功能：模块名.功能名
# # 输出test01模块中name的值
# from pack01 import test01
# print(test01.name)
"""
    如果_init_.py文件中没有定义_all_变量或显式地导入包内的任何模块或子包，
    那么执行from包名 import*时，它只会导入_init_.py文件中直接定义的内容
    （如函数、类、变量等），而不会导入其他包内的其他模块或子包
    _all_变量：是一个列表，用于模块和包中控制from...import*的导入行为  
    _all_ =  [test01, test02]
注：在_init_中，使用_all_列表，列表中的元素（模块名），要提前导入
    from . import test01
    _all_ = ["test01", "test02"]
    在模块定义_all_列表时，使用from模块名import* 将导入该列表中指定的元素
    （如函数、类、变量等）。同样地，当在包下的_init_.py 文件中定义_all_
    列表时，执行from包名import* 将仅导入该列表中明确指定的模块（如果列表中包含模块名）
    或_int.py_文件中直接定义的其他名称（如函数、类等）
"""
from pack01 import *
print(test01.name)  # NameError: name 'test01' is not defined




