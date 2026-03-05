# print("很好1")
# print("很好2")
# print("很好3")
# print("很好7")
# print("很好")
# print("很好4")
# from ctypes import HRESULT


"""print(self,*agrs,sep = '',end = '/n'，file = None)
arg:参数（可输入多个参数，数字逗号隔开，字符串双引号再加逗号隔开），
字符串参数必须是被定义（视为数据），否则识别变量名，报错
sep:设置sep参数，作为参数间隔的参数，default“空格”
end:设置输出结尾参数，default“/n”(换行)
"""
#print(123,456,"bingbing",sep="2",end=" @ ")
#print(127,458,sep=" @ ")
#print("很好",end="#")

'''变量赋值:左变量，右数值或表达式
    先赋值后使用'''
'''字符串加引号=字符串
字符串不加引号（未定义）= 变量'''
'''数字也区分大小写'''

"""数值类型 四类"""
"""（1）整数型int"""
#num = 15  # 定义整型
#print(num,type(num))  # 输出num的值，类型
"""（2）浮点型float"""
#pi = 3.1159  # 定义浮点型
#print(pi, type(pi))  # 输出pi值，类型
"""（3）布尔型型bool"""
#V1 = True  # 定义bool型
#print(V1,type (V1))  # 输出V1，类型
#V2 = False  # 定义bool型
#print(V2,type(V2))  # 输出V2，类型
"""bool型被隐形视为整数类型
         True为1
         False为0"""   # 英文符号
#result = True + 2
#print(result)
#result = False * 3
#print(result)
"""（4）复数型complex"""
#c = 2 +3j  #定义负数，j作为虚数特有的部分组成，不可更改
#print(c,type(c))  # 输出c的值，类型

"""字符串str"""
'''单引号，双引号，三单引号，三双引号'''
#S1 = 'Hellow World'
#print(S1,type(S1))
#S2 = "Hellow World"
#print(S2,type(S2))
#S3 = '''Hellow World'''
#print(S3,type(S3))
#S4 = """Hellow World"""
#print(S4,type(S4))

'''格式化输出'''
'''（1）旧式操作符号%'''
'''调用print函数
    print("args:%s",%,variable) 注：“：”指示；%s 字符串类型；%，执行格式操作；variable,目标变量）
    print("参数：类型"，格式操作，（针对）变量操作并带入)'''
#name = 'wang'
#print("我的名字：%S",% name)
'''(2)新式字符串格式化str.format(variable,...)'''
'''调用print函数,format函数，占位符{}
        print("args:{},...",format(vaiable,...))
        print("参数：占位符,...",format函数依次将变量插入占位符)'''\
        '''根据数据，输出我的名字，我的年龄,我的性别'''
#name = 'wang'
#age =  18
#sex = '女'
#print("我的名字：",name,",我的年龄：",age,",我的性别：",sex,sep='')  # 简单调用print函数，注意sep位置，以及需要加的逗号
#print("我的名字：{},我的年龄：{},我的性别：{}".format(name,age,sex))  # 使用str.format，注意 “.”不是“,”
#print("我的名字：{name},我的年龄：{age},我的性别：{sex}".format(name = name,age = age,sex = sex))  # 使用{}调用
'''（3）f-strings字符串格式方法'''
'''（3.1）通过在字符串前加上F或f来标识，允许在字符串直接嵌入表达式。表达式被大括号{}包围，其计算结果被转换为字符串并查人到相应位置'''
#name = "wang"
#age = 18
#sex = '女'
#print(f"我的名字:{name}，我的年龄：{age},我的性别：{sex}")
'''（3.2）支持表达式'''
#n1 = 2
#n2 = 3
#print(f"{n1}*{n2}={n1*n2}")  # {}注入
'''（3.3）设置整数位数'''
'''注：{}，需要填写变量，并书写“：”规则，（默认空格，可使用0）【03d或3d】保留位数“3”，并指明数值“d”类型'''
#sid = 1
#print(f"学位号：{sid:3d}")  # “：”书写规则；“3d” 设置保留三位整数
#print(f"学位号：{sid:03d}")  # “03d” 设置保留三位整数，不足补零
#print(f"学位号：123")
'''(3.4)保留小数精度'''
'''注：{}，需要填写变量，并书写“：”规则，表明小数点“.”后，保留位数“3”，并指明数值“f”类型'''
#num = 1.5
#print(f"num保留三位小数：{num:.3f}")  # 保留三位小数，不足补零
#num = 3.1545
#print(F"num保留三位小数：{num:.3f}")  # 保留三位小数，超过四舍五入

'''算术运算符（只要涉及浮点数，结果通常也会是浮点数）
   优先级遵循数字中的标准
   (1)先乘除后加减
  （2）同级从左到右
  （3）可以使用()调整计算的优先级 
  （）>**>/* // % >+-
'''
#加法,减法，乘法，除法，整除//,取余数%，幂指数
# num = 6
# num1 = 3
# print(f"{num}+{num1}={num+num1}")  # 加法
# print(f"{num}-{num1}={num-num1}")  # 减法
# print(f"{num}*{num1}={num*num1}")  # 乘法
# print(f"{num}/{num1}={num/num1}")  # 除法：返回浮点数，除数不为零，
# print(-10//3)  # 整除：下取-4
# print(-10%3)  # 取余数：整数部分，基于取整除-10%3=-10-3*-4=2
# print(2**3)   # 幂指数：第一个数做底数，第二个数做指数=2*2*2

'''赋值运算符（左变量，右数值）：/= 结果为小数5.0'''
# 先赋值在运算，在赋值
# a = 2
# a += 3  # a = a + 3
# print(a)

'''输入函数input(-prompt = none)'''
'''intput("请输入你的姓名")运行光标闪，等待你输入，把结果赋值到变量'''
# # 参数：-prompt:提示信息，会在控制台显示可忽略
# name = input("请输入你的名字：")  # 将用户名输入，保存到变量name
# print(f"你好：{name}")
# print(name,type(name))

'''转义字符(python中转义字符用于字符串中表示那些通常具有特殊含义的字符)'''
# #(1)\t 制表符，用于对齐文本【一个单元四个字符，不满空格补齐;满四，另空四个字符】
# print("w\t*")        # w	*四个空格一单元
# print("ww\t*")       # ww	*不满四，补空格
# print("wwww\t*")     # wwww	*满4，另补空格
# print("wwwww\t*")    # wwwww	*
# #(2)/n 换行符
# print("这是第一行\n这是第二行\n这是第三行")

# #(3)\\ 反斜杠符号，用于在字符串中表示一个反斜杠
# print("D:\\tools\\pathon")  # \tools\pathon
'''注：字符串中，单引号和双引号一般只能单对出现，可同时使用替代第二个相同引号'''
# #print("he is "dog"")  # 无法识别
# print('he is "dog"')
# print("he is 'dog'")

# # （）若字符串中要使用特定引号，或存在两个相同及以上的同引号，使用转义字符\
# print("it\'possibe to escape single quotes")  # 将‘转义为字符（串）
# #【4】r 原生字符串（取消字符串转义）
# #print("C:\users\example\document")  # \u,\e,\d,转义字符
# print(r"C:\users\example\document")  # r
#print("C:\\users\\example\\document")  # //

'''if语句流程，成立执行;否则，跳过。
语句格式 if 条件表达式：
            条件成立执行的代码块
            '''
# #检查温度是否高于20度
# temperature = 25
# if temperature > 20:
#         print("高温")

'''比较运算符,成立，输出Ture；否则，输出False'''
# # 相等 == 不等 ！= 大于 >小于 <
# #大于等于>=   小于等于<=
# print(1==1)
# print(2!=2)

'''逻辑运算符，and(且) ,or（或）, not（非），
另逻辑运算符空值之说（Ture or False跳过），且有输出短路特性(输出为值非跳过)'''
# x = 0
# y = 5
# z = -5
# if x > 0 and y > 0 and z > 0: # 检查x,y,z三者是否都为正数
#     print("三者都是正数")  # False,直接跳过
# if x > 0 or y > 0 or z > 0: # 检查x,y,z三者之一是否都为正数
#     print("三者之一为正数")  # ture，输出三者之一为正数
# if not y ==5:  # 检查y是否等于5
#         print("y不是5")   #直接跳过

# # 空值性：条件为空（数值为0.字符串空等），输出为空（跳过）；否则为Ture
# x = 5
# if x:
#         print(f"{x}为非空数值")
# y = ""
# if y:
#         print(F"{y}为空字符串")  # 无输出，直接跳过
# # 短路特性：and运算符：只要一个值为0，其结果必为0：否增，输出结果为最后一个结果
# print(1 and 0)  # 0
# print(0 and 1)  # 0
# print(1 and 2)  # 2
# print(2 and 1)  # 1
# #  or运输符：一真为真，先真为果
# print(1 or 0)  #  1
# print(0 or 1)  #  1
# print(1 or 2)  #  1
# print(2 or 1)  #  2

'''if （）else ()二选一
if 条件表达式:
   条件成立，执行代码
   else:
   条件不成立，执行代码'''
#检查一个人是否成年
# age = 19
# if age > 18:
#     print("成年")
# else:
#     print("不成年")
# #检查天气是否下雨(布尔型数值)
# is_rianing = True
# if is_rianing:
#     print("带伞")
# else:
#     print("不带伞")


"""三元表达式（多行表达式转换为一行简单表达）
#处理简单结构，可读性和简洁性"""

"""if：   elif：(多选一)
if 条件表达式1:
    条件1成立，执行行代码
    elif  条件表达式1:
    条件2成立，执行行代码
    elif  条件表达式1:
    条件3成立，执行行代码
    ...
    else ：
    不满足条件，跳过
    """
# 检查天气情况，判断穿衣
# weather = "rainy"
# if weather == 'sunny':
#     print("短袖")
# elif weather == 'cloudy':
#     print("长袖")
# elif weather == 'snow':
#     print("暖衣")
# else:
#     print('情况无法判断')


'''if内嵌（外if 内if）'''
# #  同时检查成绩和出勤率，以决定是否或得奖学金
# score = 88
# attendance = 98
# if score >= 85:  # (外if)
#     print("成绩达标")
#     if attendance >= 90:（内if）
#        print("出勤率达标")
#     elif 90 > attendance >= 0 :
#        print("出勤率不达标 ")
#     else:
#       print("0")
# else:
#     print("成绩不达标")



'''while循环（条件循环）：给定条件，许可重复执行；否则，跳出循环'''
'''一次循环结束，回到while语句，进行判断，再执行循环'''
# #设置循环条件：循环5次
# i = 1
# sum = 0
# while i <= 5:
#         sum += i
#         print(sum)
#         i+=1

'''while内嵌循环
while 外部循环条件：
外循环主体
      while 内部循环条件：
      内循环主体
注：镶嵌循环具体特定的循环体系
      '''
# #依次输出三排六列
# i = 1
# while i <= 3:
#         j = 1
#         while j <= 6:
#                 print(F"第{i}排第{j}列",end = "\t")
#                 j += 1
#         print()
#         i += 1

'''for循环：针对可迭代对象（列表，字符串等），将可迭代对象的每一个元素，依次读取
   计算重复循环次数或按顺序访问序列中每一个元素
格式
for  变量 in 可迭代对象:
  循环体 
   注：单独的数值类型数据（如整数，浮点数）本身不鞥直接使用，
   可通过range函数生成数值序列在for循环中一次处理数值
针对迭代类型，数值类型，如123,生成数字序列
range(start,stop,step) 注：只包前不包后，循环到100，stop为101；
start:指定计数起始值。可以省略，则默认从0开始.              range(5)
stop:指定技术结束值，不可省略。                        rang(5)
step:指定步长，两个值之间的间隔。可以省略，如果省略步长为1. range(1,5,1)
   '''
# st = "bingbing"
# for s in st:  # 将st的每个元素读取到变量S
#         print(s,end = "")

# # 使用for循环，从1到100,（包含1，不包含101）的整数
# i = 0
# for i in range(1,101):
#         print(i)

'''for 嵌套'''
# # 输出三排六列
# for i in range(1,4):  # 可以未定义，变量
#         for j in range(1,7):
#                 print(f"第{i}排第{j}列",end = "\t")
#         print() # 默认换行

'''break and continue (不能脱离循环使用)
 break 直接脱离循环
 continue 跳过此循环，执行下一循环'''
# # 吃到第三个停止
# for i in range(1,6):
#         print(F"吃了第{i}个")
#         if i == 3:
#                 break
# #不吃第三个
# for i in range(1,6):
#         if i == 3:
#                 continue
#         print(f"吃了第{i}个")

"""else 语句（用于循环结束，报告循环的情况）
for和while循环都可与else语句使用
循环中有break语句，跳过else语句
语法结构
while 条件表达式：
循环体  # 执行循环体，若不执行则进入else
else:
循环结束执行"""
# count = 1
# while count <= 5:
#   print(f"第{count}次循环")
#   count += 1
# else:
#   print("循环结束 ")


'''字符串与机器语言
字符串与字节串（计算机二进制）
解码（encode）:将字符串转换为指定编码的字节串（自然语言转换机器语言）
编码（decode）:将指定编码的字节串转换为字符串（机器语言转换自然语言）
utf-8(python)：汉字三字节
gbk：汉字2字节

'''
# st = "你好！"
# print(st.encode("utf-8"))  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x81'
# print("st",type(st))
#
# st = b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x81'
# print(st.decode("utf-8"))  # 你好！
# print("st",type(st))  # st <class 'b ytes'>

'''字符串运算符
（1）算术运算符
“+”字符串拼接
“*”字符串重复
（2）成员运算符：检查字符串中是否包含了某个子字符串
 子字符串 in str  # 如果字符串包含子字符串，返回True；否则，返回False;
  '''
# print(1+1)  # 整数相加，“+”是算术运算符  2
# print("1"+"1")  # 字符串相加，"+"字符串拼接   11
# st1 = "舒服"
# st2 = "啊！"
# print(st1+st2)   # 舒服啊！
# print("美女"*3)  # 美女美女美女
#
# st = "bingbing"
# print("b" in st )   # True
# print("bb" in st )  # False 子字符串整体寻找
# print("bb" not in st )   # Ture

'''索引与切片
(1)字符串索引[下标]：用于快速定位并获取字符串中的位置
语法格式  str[index]
index:是一个整数参数，表示要访问的字符在在字符串中的位置
字符串的位置
从左到右：从0开始计数，超出下标保错
从右到左：从-1开始计数
print(name[0])  # b
print(name[4])  # IndexError: string index out of range

print(name[-1])  # g
print(name[-2])  # n
（2）切片：获取序列中一部分元素，切片方向：step正负数，需起止方向相同
切片操作通过指定序列的起始索引，结束索引和步长来实现，返回一个新序列，包含原序列中指定范围的元素
语法： seq[start:stop:step]
start（可选）:切片的其实索引（包含），如果省略，则默认为序列的开头
stop（可选）：切片的结束索引（不包含），如果省略，则默认为序列的结尾
step(可选)：切片的步长，如省略，则默认为1。步长的绝对值大小决定切取数据的间隔，正负号就饿顶切取方向
正数表示从左向右，附属表示从右往左取值
注：start->stop 方向需同step方向相同，否则报错'''
# name = "bing"
# print(name[0])  # b
# print(name[2])  # n
# print(name[4])  # IndexError: string index out of range

# print(name[-1])  # g
# print(name[-2])  # n

# my_string = "abcdefghijklmn"
# print(my_string[2:7:1])  # cdefg
# print(my_string[:5])  # abcde  省略start
# print(my_string[5:])  # fghijklmn 省略 stop
# print(my_string[::2])  # acegikm  省略 start ,stop
# print(my_string[1:5:-1])
# #注：start->stop 方向需同step方向相同，否则报错

'''字符串常见的内建函数
（1）查找元素（区别，找不到报错方式）包前不包后，查找（find,index）,计数（count）
【1】str.find(sub[,start[,end]])
查找子字符串中首次出现位置。如果找到子字符串，，返回第一个字符索引位置，若没有，返回-1；
sub：要查找的子字符串
start(可选):开始查找的位置。如果省略，则从字符串的开头开始查找。
end(可选)：结束查找的位置。字符串的查找会在这个位置之前停止。如果省略，增查找一直进行到字符串的末尾
【2】str.index(sub[,start[,end]])
查找子字符串中首次出现位置。如果找到子字符串，则返回其首次出现的索引；如果没有找到，报错异常
sub：要查找的子字符串
start(可选):开始查找的位置。如果省略，则从字符串的开头开始查找。
end(可选)：结束查找的位置。字符串的查找会在这个位置之前停止。如果省略，增查找一直进行到字符串的末尾
【3】str.count(sub[,start[,end]])
统计子字符串在字符串中出现的次数的次数。如果子字符串在字符串中不存在，则返回0.
sub:要统计的子字符串
start(可选):开始查找的位置。如果省略，则从字符串的开头开始查找。
end(可选)：结束查找的位置。字符串的查找会在这个位置之前停止。如果省略，增查找一直进行到字符串的末尾
'''
# name = "bingbing"
# print(name.find("g"))  # 3
# print(name.find("gg"))  # -1 不存在 整体查找
# print(name.find("ing")) #  1  返回第一个查找元素的位置
# print(name.find("b",2))  # 4
# print(name.find("i",2,6))  # 5
# print(name.find("i",2,5))  # -1  end：包前不包后

#name = "bingbing"
# print(name.index("g"))  # 3
# print(name.index("gg"))  # 报错
#print(name.index("ing")) #  1  返回第一个查找元素的位置
#print(name.index("b",2))  # 4
#print(name.index("i",2,6))  # 5
#print(name.index("i",2,5))  # 报错

# name = "bingbing"
# print(name.count("b"))  # 2
# print(name.count("bb"))  # 0不存在
# print(name.count("b",1))  # 1
# print(name.count("b",1,6))  # 1
# print(name.count("b",1,4))  # 0

'''
(2)修改元素：替换（replace），分割（split），去除首尾(strip)，大小写转换
【1】str.replace(old,new,count)
替换字符中的某些部分
old:需要被替换掉的子字符串
new:用于替换old的新字符串
count(可选):指定替换的最大次数。如果省略此参数或其值小于0，则替换操作将进行到底，即替换所有匹配的子字符串。
如果指定count的值，则只替换前count次出现的old;
【2】str.split(sep = None, maxsplit = None)
将字符串分割成列表中的子字符串。默认会根据任何空白字符（如空格，换行符\n/，制表符\t等）来分割字符串，
也可以通过指定一个分隔符来改变分割行为，如果分隔符不存在，输出整个字符
sep:分隔符默认为None,表示使用空白字符作为分隔符。如果指定了其他子字符串作为分隔符，
   则该方法会在这个指定的分隔符处分割字符串
maxsplit:可选参数，指定分割的最大次数。默认为-1，表示分割次数没有限制，即分割所有可能的字符串。
   如果只能了非负整数n，则字符串只会被分割n次，并生成一个包含n+1个元素的列表
【3】str.strip([chars])
去除字符串首尾的指定字符（默认情况下，是去除空白字符，包括空格，换行符等） 注：中间不会去除
chars(可选):要从字符串开头和末尾去除字符集合。如果未指定，将去除所有空白字符。chars的参数，一个字符串
包含要从原字符串去除的字符。strip方法会去除字符串开头和末尾出现的chars中的任意字符，直到遇到不在chars中的字符为止。
【4】str.lower()
将字符串中所有大写字母转换为小写字母
【5】str.upper()
将字符串中所有小写字母转换为大写字母
'''
# name = "hello world, hello world"
# print(name.replace("hello", "hi",1))  # hi world, hello world
#
# st = "hello world, hello world"
# print(st.split())  # 空白符 ['hello', 'world,', 'hello', 'world']
# print(st.split(","))  # 逗号 ['hello world', ' hello world']
# print(st.split(" ",1))  # ['hello', 'world, hello world']
#
# st = "hello world!"
# print(st.strip("!"))  # hello world
# st = "   hello world   !"
# print(st.strip())  # hello world
# st = "xyxhello worldyx"
# print(st.strip("xy"))  # 去除首尾x，y   hello world
#
# name = "HELlO WOrLD"
# print(name.lower())  # hello world
#
# name = "hEllo woRld"
# print(name.upper())  # HELLO WORLD

'''
（3）判断元素：判断元素前缀（start），后缀（end），字符大小写
【1】str.startswith(prefix,start[,end])
检查字符串是否以指定的前缀开始。如果字符串以指定前缀开始，则返回True;否则返回False
prefix:要检查的前缀
start(可选)：开始检查的位置。如果省略，则从字符串的开头开始检查
end(可选)：结束检查的位置。字符串的检查会在这个位置前停止。如果省略，则会一直检查到字符串
【2】str.endswith(suffix,start[,end])
检查字符串是否以指定的前缀开始。如果字符串以指定前缀开始，则返回True;否则返回False
suffix:要检查的后缀
start(可选)：开始检查的位置。如果省略，则从字符串的开头开始检查
end(可选)：结束检查的位置。字符串的检查会在这个位置前停止。如果省略，则会一直检查到字符串结尾
【3】str.isupper()
检查字符串中所有可识别的字母字符是否都是大写。如果字符串中至少有一个可识别的字母字符，并且所有这些字母字符都是大写，
肖恩返回Ture;如果字符串为空，不包含任何字母字符，或者只是包含一个小写字母字符，则返回False
【4】str.islower()
检查字符串中所有可识别的字母字符是否都是小写。如果字符串中至少有一个可识别的字母字符，并且所有这些字母字符都是小写，
肖恩返回Ture;如果字符串为空，不包含任何字母字符，或者只是包含一个大写字母字符，则返回False
'''
# st = "hello world!"
# print(st.startswith("hello"))  # Ture
# print(st.startswith("h"))   # Ture
# print(st.startswith("el"))  # False
# print(st.startswith("el",1))  # Ture
# print(st.startswith("el",2,6))  # False
#
# str = "hello world!"
# print(str.endswith("!"))  # True
# print(str.endswith("world!"))  # True
# print(str.endswith("lo",1,5))  # True
# print(str.endswith("lo",1,4))  # False
#
# st = "PATHON"
# print(st.isupper())  # True
# st = "pAthOn"
# print(st.isupper())  # False
# st = "PATHON, 3.8"
# print(st.isupper())  # True
# st = " "
# print(st.isupper())  # False
#
# st = "pathon"
# print(st.islower())   # True
# st = "pathon, 3.8"    #字符串包含字母，数字
# print(st.islower())   # True，有小写字母
# st = " "              # 不包含字母
# print(st.islower())   # False


''''''
