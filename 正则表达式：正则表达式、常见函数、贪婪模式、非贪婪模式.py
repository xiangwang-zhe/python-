"""正则表达式：正则表达式、常见函数、贪婪模式，非贪婪模式"""
import string
from _ast import pattern

'''
1.1 正则表达式：一种用于描述文本模式的代码，它定义一系列规则来匹配字符串中的特定
    模式。这些模式可以非常灵活和复杂，能够用于识别和处理各种文本数据。
    
    它是强大的字符串处理工具。在软件开发中，我们经常需要查找、验证或提取特定
符合规则的字符串。例如，在网页爬虫或数据抓取任务中，我们可能需要从大量文本中
提取所有有效的邮箱地址或电话号码。这时，正则表达式就派上了大用场，它允许我们
以一种高效且准确额定方式来完成这些任务。

    python自1/5版本开始内置了re模块，该模块提供了完整的正则表达式功能。要使用
正则表达式，首先需要导入python程序中进行正则表达式的匹配、搜索、替换等操作。
        import re   # 导入re模块

1.2 特点
    1.语法复杂性：正则表达式语法相对复杂，包含了许多特殊字符和元符号，这些字符
具有特定的含义和用途。由于这种复杂性，正则表达式的可读性通常较差，尤其是对对于
那些不熟悉其语法的开发者来说。然而，正式这种复杂性赋予了正则表达式强大的匹配能力，
能够处理各种复杂的文本模式。
    2.通用性：正则表达式的强大之处在于其通用性。几乎所有的现代编程语言都支持
正则表达式，包括但不限于Python,JavaScript、C#等。这意味这开发者可以在不同的
编程环境中使用相似的语法和规则来编写正则表达式，实现跨语言的文本处理功能。这种
通用性使得正则表达式成为处理字符串数据时，不可或缺的工具之一。

1.3 简单使用
步骤（三步）：
    1.导入模块
    代码实现：
    2.使用match()进行匹配操作。
    语法格式
    re.match(pattern, string, flags= 0)
# 用于从字符串的起始位置开始匹配正则表达式。如果匹配成功，将返回一个匹配对象
(match对象),该对象包含了匹配的信息，如匹配的文本和位置；，如果匹配失败，则
返回None。
参数说明：
    pattern:要匹配的正则表达式模式。
    string:要搜索的字符串。
    flags(可选)：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，
是否多行匹配等。如果省略，则默认为，表示不使用任何标志。

    3.匹配成功，通过 group 方法提取数据‘
注：当使用group方法时，如果匹配失败（即re.match()返回None），尝试调用 
group 将引发AttributeError。因此，在调用group方法前，应该检查匹配对象
是否为None。
'''
import re   # 导入re模块
'''从字符串的第一个字母开始匹配'''
# res = re.match('o', 'hello')
# print(res)   # None（）匹配失败
# print(res.group()) #AttributeError: 'NoneType' object has no attribute 'group'
#
# res = re.match('h', 'hello')
# print(res)   # <re.Match object; span=(0, 1), match='h'>（匹配成功）
# print(res.group())    # h

# res = re.match('0', 'hello')
# if res is not None:
#     print(res.group())
# else:
#     print("匹配失败")

"""1.正则表达式"""
'''
匹配单个字符：在正则表达式中，匹配单个字符的元子符和字符类提供了灵活的方式来
指定要匹配的字符范围。

所谓的匹配单个字符，就是匹配的字符，
从前往后，依次匹配，匹配一次，无论成功还是失败，都输出

'.':匹配任意一个字符（除了\\n）
'[]':匹配[]中列举的字符
'\\d':匹配数字，0-9
'\\D':匹配非数字，即不是数字
'\\s':匹配空白。即空格tab键
'\\S':匹配非空白
'\\w':匹配单调字符，即a-z,A-Z,0-9
'\\W':匹配非单调字符
'''
''' 1 "."：匹配除了换行符（r'\\n'）以外的任意字符'''
# res = re.match('.','哈哈')
# print(res.group())

# res = re.match('.','\n')
# print(res.group())
# # AttributeError: 'NoneType' object has no attribute 'group'

'''2 '[]':匹配[]中列举的字符'''
'''从头开始匹配[i],match'bingbing',报错；match'ingbing',输出i '''
# res = re.match('[i]','ingbing')
# print(res.group())
'''匹配连续字符'''
'''从列表中依次提取单个字符与match中的字符匹配，
每个从列表中提取的字符与需要match的字符从前到后匹配
最先匹配到的字符，之后退出'''
# # res = re.match('[ing]','ingbing')
# # print(res.group())
#
# res = re.match('[0123456789]','3')
# print(res.group())
# # 简化
# res = re.match('[0-9]','9')
# print(res.group())

# 需求：匹配除5之外的任意一个数字字符
# res = re.match('[0123456789]','012346789')
# print(res.group())

# res = re.match('[0-46-9]','3')
# print(res.group())

'''
匹配任意一个小写字母字符：[a-z]
匹配任意一个大写字母字符：[A-Z]
匹配任意一个字母字符：[a-zA-z]

'''

'''3 r'\\d':匹配一个数字字符。等价与[0-9]'''
# res = re.match('\\d','0123456789')
# print(res.group())  # 0
# res = re.match('\\d','a')
# print(res.group())
# # AttributeError: 'NoneType' object has no attribute 'group'

'''4 "\\D":匹配一个非数字字符。等价于[^0-9]'''
# res = re.match('\\D','ab阿贝')
# print(res.group())  # a
#
# res = re.match('\\D','0')
# print(res.group())  # a
# # AttributeError: 'NoneType' object has no attribute 'group'

'''5 '\\s':匹配任意一个空白字符，包括空格、制表符、换行符等等 '''
# res = re.match('\\s', '\n')
# print(res.group())

'''6 '\\S':匹配任意一个非空白字符，包括空格、制表符、换行符等等 '''
# res = re.match('\\S', '\n')
# print(res.group())

'''7 \\w:匹配任意一个单词字符，包括数字、字母、汉字、_(下划线)'''
# res = re.match(r'\w','1')
# print(res.group())

# res = re.match(r'\w','@')
# print(res.group())
# AttributeError: 'NoneType' object has no attribute 'group'

'''8 '\\W':匹配任意非单词字符'''
# res = re.match(r'\W','@')
# print(res.group())

"""匹配多个字符：在正则表达式中，匹配多个字符的量词允许指定前一个字符或字符集合出现的次数"""
'''
所谓的匹配多个字符：是指在匹配字符里，
从前往后，依次匹配，匹配成功输出，继续匹配，直到匹配失败，

'*':匹配前一个字符出现0次或者无限次，即可有可无
'+':匹配前一个字符出现1次或者无限次，即至少有一次
'?':匹配前一个字符出现1次或者0次，即要么有1次，要么没有
'{m}':匹配前一个字符出现m次
'(m,n)':匹配前一个字符出现从m到n次
'''
'''1 '*':匹配前一个字符出现0次或者无限次，即可有可无'''
# res =re.match(r'\d*', '12355hjfdfg45')
# print(res.group())  # 12355
'''出现次数为0，正常匹配，输出为空'''
# res =re.match(r'\d*', 'hjfdfg')
# print(res.group())  #

'''2 '+':匹配一个字符一次或多次'''
# res =re.match(r'\d+', '1hjfdfg45')
# print(res.group())  # 1
# res =re.match(r'\d*', '12355hjfdfg45')
# print(res.group())  # 12355

# res =re.match(r'\d+', 'hjfdfg')
# print(res.group())
# #AttributeError: 'NoneType' object has no attribute 'group'

'''3.'?':匹配前一个字符零次或者一次'''
# res = re.match(r'\d?', '1234abcd56789')
# print(res.group())  # 1

# res = re.match(r'\d?', 'abcd56789')
# print(res.group())  # 空格

'''4 '{m}':匹配前一个字符每次'''
'''从前到后依次匹配m次，若中间匹配失败，增输出报错'''
# res = re.match(r'\d{4}','1234a45')
# print(res.group())
#
# res = re.match(r'\d{5}','1234a45')
# print(res.group())
# # AttributeError: 'NoneType' object has no attribute 'group'

'''5 {m,n}:n和m是非负整数，其中n<=m。匹配前一个字符至少n次，但不超过m次 '''
'''{m,n}逗号后不要加空格{m, n}：前字符数少于n,报错'''
# res = re.match(r'\s{4,6}', '12365466')
# print(res.group())

"""匹配开头和结尾"""
'''
匹配开头和结尾：在正则表达式中^和$是两个非常重要的元字符，它们分别用于匹配字符串的开始和结尾。

'^':匹配字符串开头
'$':匹配字符串结尾

'''
'''1 '^':匹配字符串的开始'''
''' ^在[]中表示……取反：除了列表其中的字符，取其余任意字符'''
# res = re.match(r'^\d{4,6}', '12365466')
# print(res.group())  # 123654
#
# res = re.match(r'^\D{4,6}', 'abcd')
# print(res.group())  # abcd

# res = re.match('[hH]', 'Hh')
# print(res.group())
# # AttributeError: 'NoneType' object has no attribute 'group'
#
# res = re.match('[^hH]', 'jh')
# print(res.group())  # j

'''2 '$':匹配字符串结尾 '''
'''先匹配结尾，匹配成功，在进行正式匹配。非颠倒顺序匹配'''
# res = re.match(r'\d+', '12345')
# print(res.group()) # 12345
#
# res = re.match(r'\d+$', '12345')
# print(res.group())  # 12345
#
# res = re.match(r'\d+$', '12345a')
# print(res.group())  # 12345
# # AttributeError: 'NoneType' object has no attribute 'group'

"""匹配分组"""
'''
在正则表达式中，分组是一个强大的特性，它允许你将正则表达式的某部分视为一个整体，
并且可以对这个整体进行引用和操作。分组不仅用于组织复杂的模式，还常用于提取数据，
进行条件匹配等。

'|':匹配左右任意一个表达式
"(ab)":将括号中字符作为一个分组
'\\num':引用分组num匹配到字符串
'(?p<name>)':分组起别名
"(?p=name)":引用别名为name分组匹配到的字符串

'''
'''1 '|':匹配左右任意一个表达式（r'\\d|\\s'）'''
# res = re.match(r'\d|\s', ' 1')
# print(res.group())

'''2 '(ab)': 将括号中字符作为一个分组'''
'''  \\. :表示只匹配点（.）'''
# # res = re.match(r'\w+@qq\.com','91784283@qq.com')
# res = re.match(r'\w+@(qq|123|126)\.com','huohua@126.com')
# print(res.group())

'''3 \\num:引用分组num匹配到的字符串（分组：（\\w+），引用分组：</\\1>）'''
'''在正则表达式只能、num(其中num是一个数字)用于引用前面第num个分组匹配
到的内容。这在进行HTML标签匹配等场景时特别有用。'''

# res = re.match(r'<(\w+)>.*</\1>',"<html>login</html>")
# print(res.group())
#
# res = re.match("<（\w+）><(\w+)>login</\2></\1>", '<html><body>login</body></html>')
#

"""2.常见函数"""
'''
2.1
findall:在正则表达式中，findall()用于在字符串中查找所有（非重叠）匹配
正则表达式的子串，并返回一个列表。（从头到尾，查找所有匹配成功的）

语法格式：re.findall(pattern, string, flags= 0)
参数说明：
pattern:要匹配的正则表达式
string1:要搜索是字符串
flags(可选):标志位，用于控制正则表达式的匹配方式，如是否区分大小写，是否多
行匹配等，如果省略，默认为0，表示不使用任何标志。

sub:在正则表达式中，sub（）用于替换所有字符串中所有匹配正则表达式的部分。

语法格式：re.sub(pattern, string, count= 0, flags= 0)
参数说明：
pattern:要匹配的正则表达式模式。
repl:替换字符创或者一个函数。如果是一个字符串，那么他可以直接被用作替换文本；
如果是一个函数，那么对于每一个匹配项，该函数都会被调用，并且函数的返回值会被
用作代替文本。
string:要在其中进行替换的原始字符。
count(可选)：模式匹配后替换的最大次数，默认为0，表示替代所有的匹配
flags(可选)：标志位，用于控制正则表达式的匹配方式，如是否区分大小写，是否多
行匹配等，如果省略，默认为0，表示不使用任何标志。
'''
'''findall'''
# res = re.findall(r'\d','123abc!@#123')
# print(res)  # ['1', '2', '3', '1', '2', '3']
'''匹配三个字母字符，以三个一组，不足省去'''
# res = re.findall(r'\w{3}','pythonth')
# print(res)  # ['pyt', 'hon']

'''sub()'''
# res = re.sub('python','bingbing', 'hellopython', flags= 0)
# print(res)

# res = re.sub(r'\d', 'x', '第11天')
# print(res)  # 第xx天
#
# res = re.sub(r'\w', 'xxx', '@@第十天')
# print(res)  # @@xxxxxxxxx

'''3.贪婪模式与非贪婪模式'''
'''
贪婪模式：指正则表达式在匹配字符串时，会尽可能多的匹配字符，指导无法继续匹配
为止。默认情况下，采用贪婪模式。

非贪婪模式：指正则表达式在匹配字符串时，会尽可能少地匹配字符，只要这样的匹配
能够使整个表达式得到满足即可。使用？紧跟在量词（如*、+、{n.m}）后面来表示非
贪婪匹配。

'''
'''贪婪模式i'''
# res = re.match(r'\d*', '123456abc')
# print(res.group())

# res = re.match(r'\d+', '123456abc')
# print(res.group())  # 123456

# res = re.match(r'\d{2,5}', '123456')
# print(res.group())

'''非贪婪模式'''
res = re.match(r'\d*?', '123456abc')
print(res.group())  # 空格

res = re.match(r'\d+?', '123456abc')
print(res.group())  # 1

res = re.match(r'\d{2,5}?', '123456')
print(res.group())  # 12


