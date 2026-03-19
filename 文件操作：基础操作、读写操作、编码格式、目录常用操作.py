import os  # 导入os模块

"""文件：基础操作、读写操作、编码格式、目录常用操作"""
'''
文件：存储在某种长期存储设备（如硬盘、U盘、移动硬盘等）上的一段数据，用于持久化保存信息
作用：将内容（数据）进行存储和存放，以便程序在需要是能够直接访问和使用这些数据，
而不是需要重新生成一份新的数据。这种做法能够节省时间和资源，提高程序的效率和便捷性。

分类：
1.文本文件
2.二进制文件
注：无论是文本文件还是二进制文件，在计算机中都是以二进制形式存储的。它们的主要区别在于
内容、用途以及人类如何查看和处理它们。


'''
'''
1.2基本操作（主要包括桑基本操作）
1.打开文件：使用open函数，返回一个文件对象，默认以只读模式打开。
2.读/写文件
读：将文件内容从磁盘加载到内存中，以便程序可以处理这些数据(因为内存的读写速度
远快于磁盘).
写：将内存中的数据写入到磁盘文件中，实现数据的持久化存储。
3.关闭文件：使用 close 方法关闭文件，释放系统资源。
注：可以只打开和关闭文件，而不进行任何读取操作，但这通常不是文件的典型使用场景。


1.2 文件对象的常见方法
1.open():创建一个File(文件)对象，默认以只读模式打开
2.read(n):从文件中读取n个字符（在文本模式下）或 n 个字节（在二进制模式下）
如果未指定n，则读取整个文件内容。
3.write(s):将制定内容 s 写入文件，在写入之前，需要将数据转换为字符串
（文本模式下）或字节串（二进制模式下）
4.close():关闭文件，这是一个非常重要的方法，用于在完成文件操作后释放文件资源。

1.2.2 文件对象的常见属性
1.file.name:返回文件对象的名称（相对路径/绝对路径）。
2.file.mode: 返回文件的访问模式。
3.file.closed:返回一个布尔值，指示文件是否已关闭。

1.2.3 绝对路径&相对路径
1.绝对路劲
绝对路径：是文件或目录在文件系统重的完整路劲。从根目录（如Windows上的c:\）,
开始一直到文件或目录的路径。它提供了到达指定文件或目录的完整地址，明确无误地
指向文件位置，不受当前工作目录的影响。  
优点：（1）唯一确定文件或目录位置，不受当前工作目录的影响
     （2）在任何情况下都能准确地定位到文件或目录
缺点：（1）当文件系统结构变化或在不同系统之间迁移代码时，可能需要修改路径
     （2）路径较长，不够灵活     
     
2.相对路径
相对路径：是相对于当前工作目录的文件或目录路径，不包含完整的根路径信息。路径的
起点是当前正在访问的文件夹，即Python脚本运行的位置或是当前操作的目录
如：test.txt、.\test.txt、..\test.txt    
  test.txt     # 当前目录下的test.txt
  .\test.txt   # 当前目录下的test.txt
  ..\test.txt  # 上一集目录下的test.txt
  
优点：（1）相对简洁，更具有灵活性，适用于在项目内部进行文件操作。
     （2）是文件结构更清晰，简化文件访问命令
缺点：（1）如果更改了工作目录，可能导致路径无效
     （2）是文件结构更清晰，简化文件访问命令  
     
应用场景：项目内部
        适用包，模
'''
'''绝对路径'''
# 需求：编写一个python程序，打开并随后关闭test.txt
# 打开文件
# f = open("test.txt")
# print(f)
# # 访问文件名称
# print(f.name)
# # 访问模式
# print(f.mode)  # "r"默认以只读模式打开
# # 关闭前，检测文件是否已关闭
# print(f.closed)   # False
# # 关闭文件
# f.close()
# # 关闭后，检测文件是否已关闭
# print(f.closed)   # True

# # 需求:使用绝对路径打开并随后关闭当前目录下的 test.txt 文件
# # 打开文件
# f = open(r"D:\pythonstudy\核心编程\test.txt")
# # 文件名称
# print(f.name)
# # 关闭文件
# f.close()

# # 需求2：使用绝对路径打开并随后关闭上一级目录Pythonstudy 下的test.txt文件
# #  D:\pythonstudy\test.txt
# # 打开文件
# f = open(r"D:\pythonstudy\test.txt")
# # 文件名称
# print(f.name)
# # 关闭文件
# f.close()
'''相对路径'''
# # 需求：使用相对路径打开并随后关闭当前目录下的 test.txt 文件
# # 打开文件
# f = open(r'.\test.txt')    # 当前路径下test，txt
# # 文件名称
# print(f.name)
# # 关闭文件
# f.close()

# 需求2：使用相对路径打开并随后关闭上一级目录下的 test.txt 文件
# # 打开文件
# f = open(r'..\test.txt')    # 上一级目录路径下test，txt
# # 文件名称
# print(f.name)
# # 关闭文件
# f.close()


"""2.读写操作"""
'''
2.1文件读取
read(n):从文件中读取 n 个字符（在文本模式下）或 n 个字节（在二进制模式下）。
        如果未指定n,则读取整个文件内容
注:使用 read 方法读取文件时，会将文件的所有内容一次性加载到内存中，这对于非
常大的文件来说，可能会给系统内存带来沉重的压力。为了更有效地管理内存资源，推荐
在处理大文件时采用 readline 方法，以便诼行读取文件内容，减少内存占用。
        
readline():从文件中读取一行内容，读取完一行后，文件指针会自动移动到下一行的
            开头，准备下一次读取。
readlines():从文件中读取所有行，并将这些行作为一个列表返回，列表中的每个元素
            都是文件中的一行。
注：如果文件非常大，使用read或readlines 方法可能会消耗大量的内存，因为它
需要将整个文件内容都加载到内存中。 
            

'''
'''读取文件'''
'''f.read（）'''
# # 打开文件
# f = open(r'..\test.txt')    # 上一级目录路径下test，txt
# # 文件名称
# print(f.name)
# # 读取文件
# print(f.read(5))           # 读取5个字符
# # 关闭文件
# f.close()

# # 需求：编写一个python程序，对当前目录下的 test.txt 文件进行读取操作
# # 打开文件
# # f = open(r'test.txt')
# f = open(r'，/test.txt')
# # 读取文件
# print(f.read())           # 读取5个字符
# # 关闭文件
# f.close()
'''f.readline（）'''
# # 打开文件
# f = open(r'./test.txt')
# # 读取文件
# # print(f.readline())           # 读取第一行
# # print(f.readline())           # 读取第二行
# # print(f.readline())           # 读取第三行
# # print(f.readline())           # 读取第四行，但文件只有三行，所以返回空字符
#
# # 循环次数未知，结束条件已知 ==" "
# while True:
#     test = f.readline()
#     # 判断读取内容是否为空（字符）
#     if test == "":
#         # 退出循环
#         break
#     print(test)
# # 关闭文件
# f.close()
'''f.readlines（）'''
# # 打开文件
# f = open(r'test.txt')
# # 读取文件
# text = f.readlines()
# print(text,type(text))
#
# # 遍历列表
# for row in text:
#     print(row)
# # 关闭文件
# f.close()

'''
2.2 文件写入操作
在python中，向文件写入内容时，需要注意文件的访问模式            
 
2.2.1 访问模式
1.'r':只读模式（默认模式）。文件必须存在，否则报错。只能读，不能写。
2.'w':只写模式：文件不存在则创建文件，文件存在则覆盖文件（即删除文件内容并
从头开始写入）。只能写，不能读。
3.'a':追加模式。文件不存在则创建文件，文件存在则写入数据会被追加到文件末尾
只能写，不能读。
4.'+':读写模式。这个符号可以添加到'r''w''a'之后，以允许文件同时进行读写操作
 注：适用'+'会影响文件的读写效率，开发中更多时候会一只读、只写的方式来操作文件
 'r+':文件必须存在，否则报错
 'w+':文件不存在，则创建新文件，文件存在则覆盖文件（即删除文件内容并从头开始写入）
 'a+'：文件不存在，则创建新文件，文件存在，则写入数据会被追加到文件末尾。
注：文件指针的当前位置决定了下一次读取或写入操作将从哪里开始。


'''
'''r:只读模式'''
# # 打开文件
# f = open('test.txt', 'r')
# # 读取操作
# print(f.read())
# # 写入操作
# try:
#     f.write("shuihua")
# except Exception as e:
#     print("错误信息",e)
# finally:
#     # 关闭文件
#     f.close()
#
# # 打开文件
# f = open('test.txt', 'r')
# try:
#     f.write("shuihua")   # io.UnsupportedOperation: not writable
#
# finally:                # 确保文件最终能能关闭
#     # 关闭文件
#     f.close()

'''w:只写模式'''
# # 打开文件
# f = open('test.txt', 'w')
# # 读取操作
# try:
#    f.read()      # io.UnsupportedOperation: not readable
# finally:
#     # 关闭文件
#     f.close()

# # 打开文件
# f = open('test01.txt', 'w')
# # 写入操作
# f.write('hello')    # 删除文件内容并从头开始写入
# # 关闭文件
# f.close()

'''a:追加模式。'''
# # 打开文件
# f = open('test02.txt', 'a') # 打开不存在的文件
# # 写入内容
# f.write('shuihua')    # 删除文件内容并从头开始写入
# # 关闭文件
# f.close()

# # 打开文件
# f = open('test02.txt', 'a') # 打开不存在的文件
# # 读取内容
# try:
#    print( f.read()) # io.UnsupportedOperation: not readable
# finally:
#     # 关闭文件
#     f.close()

# # 打开文件
# f = open('test03.txt', 'a+')
# # 写入操作
# f.write("ssrr")
# # 读取文件
# print(f.read())  # 读取空内容，涉及到文件指针
# # 关闭文件
# f.close()
'''
2.2.2文件定位操作
1.tell():返回文件指针的当前位置
2.seek(offsset,whence == 0):移动文件指针到指定位置。
offset:偏移量，表示要移动的字节数。
whence:用于指定 offset 的起始位置（参考点），默认值是0。0代表将文件开头作为
参考位置；1代表将当前位置作为参考位置，2代表将文件结尾作为参考位置。
注：通常使用 seek（0， 0）以将文件指针移动到文件开头。
'''
# # 打开文件
# f = open('test03.txt', 'a+')
# # 获取移动前文件指针当前位置
# print('移动之前',f.tell())
# # 将文件指针移动到文件开头
# f.seek(0, 0)
# # 获取移动后文件指针当前位置
# print('移动之后',f.tell())
# # 读取文件
# print(f.read())  # 读取空内容，涉及到文件指针
# # 关闭文件
# f.close()

'''with语句'''
'''
如果每次按照open（）...close()这种方法去写文件操作代码，会显得非常繁琐。为了
简化这一过程并确保资源得到正确管理，python引入了with语句。使用with语句时，
系统会自动在代码块执行完毕后调用close方法，从而省去了手动关闭文件的步骤，使
代码更加简洁且安全。
'''
# 打开文件
# with open("test.txt","r") as f:
#     #读取文件
#     print(f.read())
#
# # 检测文件的关闭状态
# print(f.closed)

'''3.编码格式'''
'''Python3中的 open 函数相比Python2 增加了一些参数，其中最重要的新增参数
之一就是encoding。这个参数允许你指定或明确文件内容的字符编码，这对于处理文件
尤其重要，因为不同的操作系统和地区可能使用不同的默认编码来存储文件。

python的文件操作中，虽然可以省略encoding参数让open函数使用默认编码（与平台
相关，如windows系统上默认编码为 GBK ），但为了避免由于编码不一致导致的乱码
问题，特别是在处理包含文字符的文件时，强烈建议明确指定 encoding = 'utf-8'
作为文件的字符编码。



'''
# # 打开文件
# with open("test.txt",'w') as f:
#     # 写入操作
#     f.write("你好呀！")
# # 乱码 需要将CBk(默写编码)改成UTF-8

# 打开文件
with open("test.txt",'w', encoding = "utf-8") as f:
    # 写入操作
    f.write("你好呀！")

# # 打开文件
# with open("test.txt",'r') as f:
#     # 读取操作
#     print(f.read())
# #UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 8: illegal multibyte sequence

# # 打开文件
# with open("test.txt",'r', encoding = "utf-8") as f:
#     # 读取操作
#     print(f.read())

"""4.目录常用操作"""
'''
1.文件或目录重命名：os.rename(源文件或目录的路径，目标文件或目录的新路径)
(1)重命名文件：文件或目录必须存在，否则报错
(2)移动文件到另一个目录：不支持夸文件系统（夸盘）的重命名操作，即将文件从一个文件系统移动到另一个文件系统

2.删除文件：os.remove(要删除的文件的文件路径)
在删除文件之前，请确保确实想要删除该文件，因为一旦删除，就无法恢复（除非有备份）

3.创建目录：os.mkdir(要创建的目录路径)
创建目录前，必须确保该目录不存在，否则将会报错 fileExistsError

4.删除目录：os.rmdir(要删除的目录路径)
在删除文件之前，请确保确实想要删除该文件，因为一旦删除，就无法恢复（除非有备份）
删除目录之前，请确保确实想要删除该目录，并且该操作符合马倩策略。删除目录是一个不可逆的操作
，一旦执行，就无法恢复已删除的数据（除非有备份）

5.获取当前工作目录：os.getcwd()
该功能在需要知道当前工作目录以便进行文件操作（如读取或写入或删除文件）时非常有用

6.获取目录列表：os.listdir(要获取的目录路径)
():默认获取当前工作目录，可指定获取工作目录下的所有工作目录和文件
print(os.listdir(r'D:\pythonstudy'))

7.检验路径是否存在：os.path.exists(要检查的路径)
相对路径
绝对路径

8.检验路径是否存在且为文件：os.path.isfile(要检查的路径)

9.检验路径是否存在且为目录：os.path.isdir(要检查的路径)

'''
'''4.1.文件或目录重命名：os.rename(源文件或目录的路径，目标文件或目录的新路径)'''
'''文件或目录必须存在，否则报错'''
# # 重命名文件
# os.rename("image[备份].png","image2.png")
# # 将当前目录下名为"image【备份】.png"的文件重命名为"image2.png"

'''不支持夸文件系统（夸盘）的重命名操作，即将文件从一个文件系统移动到另一个文件系统'''
# # 移动文件到另一个目录
# os.rename("image2.png", r"D:\pythonstudy\image2.png")
# # 将当前目录下名为“image2.png”的文件移动到“D:\pythonstudy\image2.png”

'''4.2 删除文件：os.remove(要删除的文件的文件路径)'''
'''在删除文件之前，请确保确实想要删除该文件，因为一旦删除，就无法恢复（除非有备份）'''
# # 删除当前目录下的test03.txt文件
# os.remove("test03.txt")

# # 删除D:\pythonstudy目录下的image2.png的文件
# os.remove("D:\pythonstudy\image2.png")

# try :
#     os.remove(r"D:\pythonstudy\image2.png")
# except Exception as e :
#     print("错误信息", e)
# # 错误信息 [WinError 2] 系统找不到指定的文件。: 'D:\\pythonstudy\\image2.png'

'''4.3 创建目录：os.mkdir(要创建的目录路径)'''
'''创建目录前，必须确保该目录不存在，否则将会报错 fileExistsError'''
# # 在当前目录下创建一个名为“bingbing”的目录
# os.mkdir("bingbing")

# 在D盘创建“bingbing”目录
# os.mkdir(r"D:\bing")

# try:
#     os.mkdir(r"D:\bingbing")
# except Exception as e:
#     print("错误信息", e)
# # 错误信息 [WinError 183] 当文件已存在时，无法创建该文件。: 'D:\\bingbing'

"""4.4删除目录：os.rmdir(要删除的目录路径)"""
# '''只能删除空目录。如果目录包含文件或其他目录，则要先删除这些内容'''
# # 在当前目录下创建一个名为“bingbing”的目录
# os.rmdir("bingbing")

'''4.5获取当前工作目录的绝对路径：os.cwd(当前工作目录)'''
# # 获取当前工作目录
# print(os.getcwd())

'''4.6获取目录列表：os.listdir(要获取的目录路径)'''
# # 获取当前目录下的所有文件和目录
# print(os.listdir())
#
# # 获取指定目录下的所有文件和目录
# print(os.listdir(r'D:\pythonstudy'))

'''4.7 检验当前目录是否存在：os.path.exists()'''
# # 检查文件/目录是否存在
# # 相对路径（当前目录）
# print(os.path.exists(r'test.txt'))  # Ture
# print(os.path.exists(r'test【备份】.txt'))   # False
#
# # 绝对路径
# print(os.path.exists(r'D:\pythonstudy'))    # Ture

'''4.8 检验路径是否存在且为文件：os.path.isfile(要检查的路径)'''
# # 检验路径是否存在且为文件
# # 相对路径
# print(os.path.isfile('test.txt'))   # True
# # 绝对路径
# print(os.path.isfile(r'D:\pythonstudy'))  # False

'''4.9 检验路径是否存在且是否为目录'''
# # 检验路径是否存在且为目录
# # 相对路径
# print(os.path.isdir('test.txt'))   # False
# # 绝对路径
# print(os.path.isdir(r'D:\pythonstudy'))  # True

"""
案例：图片备份（图片复制）
之前讲解侧重于文本操作，然而，在处理诸如图片、视频等二进制文件时，我们必须在
访问模式字符串中明确加入‘b’标志（如使用‘rb’进行读取、'wb'进行写入等），以
此指示python以二进制模式执行操作。这样做确保了python能够直接按照文件的原始
字节流进行处理，以避免了不需要的字符编码转换，从而实现了对二进制数据的正确且
高效管理。
"""
#  打开原元件
with open('05.png','rb') as f:
    # 读取操作
    img = f.read()
    print(img, type(img))  # <class 'bytes'>

# 将读取到的内容写入到新文件
with open('image[备份].png','wb') as f:   # 打开一个新文件
    # 写入内容
  f.write(img)




