"""线程：多任务。多线程，线程同步，互斥锁"""
'''
多任务：同一个时间段内执行多个任务
python中实现多任务处理的主要三种方式：
      线程，进程，携程
      
进程和线程（一个程序一个进程，一个进程可包含多个线程）
进程：打开一个程序至少就会有一个进程，是操作系统进行资源分配的基本单元。
线程：线程是CPU调度的基本单位，每个进程至少都有一个线程，这个线程通常就是我们
所说的主线程。一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在
进程里面的，没有进程就没有线程。

多线程
多线程：允许程序在同一时间内运行多个线程，是pathon中实现多任务的一种方式。

import time  # 导入time模块
# 导入线程模块
import threading

线程类：Thread常见参数
1.target:指定子线程要执行的任务，即要运行的函数
2.agrs:以元组的形式给执行任务传参。
3.kwargs:以字典的形式给执行任务传参。 字典的键名等于函数参数
      
'''
import time  # 导入time模块
# 导入线程模块
import threading
# 从线程模块中导入Thread类
from threading import Thread,Lock

# # 定义函数
# def sing():
#     print("我在唱歌")
#     time.sleep(2) # 暂停两秒
#     print("唱完歌了")
# def dance():
#     print("我在跳舞")
#     time.sleep(2)
#     print('跳完了')
#
# # sing()
# # dance()
#
# # 主程序入口
# if __name__ == "__main__":
#     # 创建子线程（注：子线程的次数没有限制，且彼此独立）
#     # targe:线程执行的函数名
#     '''与拷贝相似'''
#     t1 = threading.Thread(target=sing)  # 唱歌的子线程
#     t2 = threading.Thread(target=dance)  # 跳舞的子线程
#     print(t1)
#     print(t2)
#
#     # 开启子线程
#     t1.start()
#     t2.start()

# def sing(name):
#     print(f"{name}在唱歌")
#     time.sleep(2) # 暂停两秒
#     print("唱完歌了")
# def dance(name):
#     print(f"{name}在跳舞")
#     time.sleep(2)
#     print('跳完了')
#
# # 主程序入口
# if __name__ == '__main__':
#     # 创建子线程
#     # t1 = threading.Thread(target=sing, args=('susu',))    # 以元组形式为任务传参
#     # t2 = threading.Thread(target=dance, args=('shuihua',))   # 以元组形式为任务传参
#
#     t1 = threading.Thread(target=sing, args=('susu',),)  # 以元组形式为任务传参
#     t2 = threading.Thread(target=dance, kwargs={'name':'shuihua'})  # 以元组形式为任务传参
#
#     # 开启子线程
#     t1.start()
#     t2.start()

"""2.多线程"""
'''
多线程特点：（1）线程之间是无序的
          （2）线程之间共享资源
          （3）资源竞争
          
线程之间执行是无序的
线程之间执行是无序的，它有CPU调度决定的，CPU调度那个线程，那个线程就先执行，
没有调度的线程不能执行

阻塞主线程：主线程等待写入线程执行完成以后代码再继续往下执行
先执行子线程（ wd.join()），执行完再执行主线程（rd.start()）

'''

# def task():
#     time.sleep(1)
#     print("当前线程是：",threading.current_thread().name)  #显示当前线程名
#
# # 主程序入口
# if __name__ == '__main__':
#     for i in range(5):
#         # 创建子线程
#         t = threading.Thread(target=task)
#         # 开启子线程
#         t.start()

# li = []
# # 写入数据
# def write_data():
#     for i in range(5):
#         li.append(i)
#         time.sleep(i) # 暂停1秒
#     print("写入数据",li)
#
# # 读取数据
# def read_data():
#     print("读取数据", li)
#
# # 主程序入口
# if __name__ == '__main__':
#     # 创建子线程，简化
#     wd = Thread(target=write_data)
#     rd = Thread(target=read_data)
#
#     # 开启子线程
#     wd.start()
# 
#     '''阻塞主线程：主线程等待写入线程执行完成以后代码再继续往下执行
#     先执行子线程（ wd.join()），执行完再执行主线程（rd.start()）
#     '''
#     wd.join()
#
#     rd.start()
#
#     rd.join()
#
#     print("这是最后一行")

'''资源竞争'''
'''
资源竞争：当多个线程同时访问或修改同一资源时，就会产生竞争现象，这类似于多个
男生同时追求同一个女生，存在激烈的竞争关系

两个线程同时运行，资源竞争会导致输出结果与实际但线程运行结果不同
'''
# 定义全局变量
# a  = 0
# def add():
#     for i in range(10000000):
#         global a  # 声明全局变量
#         a +=1
#     print("第一次",a)
#
#
# def add2():
#     for i in range(10000000):
#         global a  # 声明全局变量
#         a += 1
#     print("第二次",a)
#
# # add()
# # add2()
#
# # 主程序入口
# if __name__ == '__main__':
#     #创建子线程
#     t1 = threading.Thread(target=add)
#     t2 = threading.Thread(target=add2)
#
#     # 打开线程
#     t1.start()
#     t2.start()


"""3.线程同步"""
'''
线程同步：以两个线程为例：线程A负责写入数据，而线程B负责读取线程A所写入的数据
这种情况下，为确保数据的准确性和一致性，必须确保线程A完成写入操作后，线程B才能
进行读取。这种确保线程A和线程B按序、协调执行的关系，就是我们所说的线程同步。
通过线程同步，我们能够避免数据竞争和不一致的问题，从而确保程序的稳定性和可靠性。

方式
1.线程等待
使用name.join（）延迟主程序执行
2.互斥锁
互斥锁：对共享数据进行锁定，确保多个线程访问共享数据不会出现数据错误问题：保证
同一时刻只能有一个线程去操作。
注：互斥锁并非静态分配，而是由多个线程动态竞争获取。成功获取锁的线程将先行执行
相关操作，而未获取锁的线程则需耐心等待。直到持有锁的线程释放后，其他等待的线程
才有机会再次竞争这把锁，进而执行自己的操作。这种机制确保了多线程环境下的数据
访问既安全又有序。


方法：
acquire():上锁。若锁当前被其他线程持有，则调用此方法的线程将被阻塞，直到锁
被释放为止。在某些情况下，你也可以为acquire方法设置一个超时时间，以避免
无限期地等待锁
release():释放锁。持有锁的线程调用此方法后，其他被阻塞、整袋等待此锁的线程
将有机会获取锁。

注：这两个方法必须成对出现，否则容易形成死锁。死锁会导致程序停歇


'''
'''线程等待（join函数）'''
# 全局变量
# a = 0
#
# def add():
#     for i in range(1000000):
#         global a    # 声明全局变量
#         a +=1
#     print("第一次：",a)
#
# def add2():
#     for i in range(1000000):
#         global a
#         a +=1
#     print("第二次：", a)
#
# # 定义端口
# if __name__ == '__main__':
#     # 创建线程
#     t1 = Thread(target=add)
#     t2 = Thread(target=add2)
#
#     # 开启线程
#     t1.start()
#     # 线程等待 join
#     t1.join()
#
#     # 开启线程
#     t2.start()

'''互斥锁（上锁：acquire（）  解锁：release（） ）'''
# # 全局变量
# a = 0
#
# # 创建全局互斥锁 from threading import Lock
# lock = Lock()
#
# def add():
#     # 上锁
#     lock.acquire()
#     for i in range(1000000):
#         global a    # 声明全局变量
#         a +=1
#     print("第一次：",a)
#     # 释放锁
#     lock.release()
#
# def add2():
#     # 上锁
#     lock.acquire()
#     for i in range(1000000):
#         global a
#         a +=1
#     print("第二次：", a)
#     #解锁
#     lock.release()
#
# # 定义端口
# if __name__ == '__main__':
#     # 创建线程
#     t1 = Thread(target=add)
#     t2 = Thread(target=add2)
#
#     # 开启线程
#     t1.start()
#
#     # 开启线程
#     t2.start()

