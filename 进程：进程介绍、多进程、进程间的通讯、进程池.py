"""进程：进程介绍、多进程、进程间的通讯、进程池"""
'''
1.进程介绍：一个正在运行的程序或者软件就是一个进程，它是操作系统进行资源分配
和调度的基本单位。也就是说每启动一个进程，操作系统都会给其分配一定的运行资源
（如内存、网络连接等）保证进程的运行。
注：一个程序运行后至少会生成一个进程，一个进程默认包含一个线程，进程里面可以
创建多个线程，线程是依附在进程里面的，没有进程就没有线程。

进程状态
就绪态：已经具备执行条件，正在等待CPU的调度以开始执行。例如，一个已经加载到
内存中并准备好执行的计算器程序，它正在等待CPU分配空余时间片来启动计算任务。

执行态：cpu正在执行其功能。例如，一个正在播放视频的进程，此时cpu正在处理视频
帧的解码和渲染工作，以确保视频能够流畅播放。

等待态：正在等待某一事件或条件的发生。例如，一个王爷浏览器进程，可能正在等待
用户输入来继续执行后续操作。

除了上述三种基本状态，进程还可能经历其他状态，如挂起态和终止态：

挂起态：被操作系统暂时停止执行，这通常是为了节省内存资源或等待外部事件。例如，
当一个手机中的应用程序在后台运行时，它可能会被挂起，以释放cpu和内存资源给前台
运行的应用程序。当用户再次切换到该应用程序时，它会被恢复执行。

终止态：已经执行完毕或被操作系统强制终止。例如，一个计算器程序进程在完成计算
任务并输出结果后可能会进入终止态，或者一个因为崩溃而被操作系统强制关闭的游戏
进程也会进入终止态，此时，进程会释放其他占用的所有资源，以供其他进程使用。

'''
'''
2.多进程
    multiprocessing 模块是一个夸平台的多进程管理模块，它定义了process
类来创建并管理独立的进程对象，这些进程队形能够并行地执行不同的任务。

子进程与主进程
若子进程只是简单的创建和开始，程序会优先执行主进程程序

2.1 进程语法结构
2.1.1 Process类常见参数
target:指定子进程要执行的任务，即要运行的函数
args:以元组的形式给执行任务传参（args=("bingbing",)）
kwargs:以字典的形式给执行任务传参(kwargs={"name":"bingbing"})
健名：形参   键值：实参

2.1.2 Process 类常见方法
(1)start():开启子进程
(2)is_alive():检查子进程是否仍然运行。如果子进程仍然在运行，则返回Ture；如果
子进程已经终止，则返回False.
(3)join():阻止主进程，即主进程等待子进程执行结束。

未使用join(),主进程优先，子进程存活状态为Ture
使用join()，阻碍主程序，优先子程序（p1.join()）,子进程存活状态为False

2.1.3 Process 类常见属性
(1)name:当前进程的别名（程序默认进程名称：对象名.name）  p1.name
修改子进程名两种方法：
1.实例化对象中修改
 # p1 = Process(target=sing, name = "p1",args=("bingbing",))
 2.实例化对象后
     p1.name = "pro1"
     
(2)pid:当前进程的进程编号（程序默认进程编号 ：对象名.pid）
    # 访问子进程的进程编号
    print("p1子进程编号：",p1.pid)
    # 访问父进程（子进程：os.getpid()  父进程：os.getppid()）
    print(f"sing子进程ID：{os.getpid()}")       ppid
    print(f"sing子进程ID：{os.getpid()}, 父进程ID:{os.getppid()}")
'''
from multiprocessing import Process, Queue, Pool  # 进程模块里面自带 Queue
import os
import time
#
# # 唱歌任务
# def sing(name):
#     print(f"{name}在唱歌")
#     # 访问父进程
#     print(f"sing子进程ID：{os.getpid()}, 父进程ID:{os.getppid()}")
#
# # 跳舞
# def dance(name):
#     print(f"{name}在跳舞")
#     # 访问父进程
#     print(f"sing子进程ID：{os.getpid()}, 父进程ID:{os.getppid()}")
#
# # 主程序入口
# if __name__ == '__main__':
#     # 创建子进程
#     p1 = Process(target=sing, args=("bingbing",))
#     p2 = Process(target=dance, kwargs={"name":"bingbing"} )
#
#     # p1的子进程名是： Process - 1
#     # p2的子进程名是： Process - 2
#
#     '''修改子进程名：第一种'''
#     # p1 = Process(target=sing, name = "p1",args=("bingbing",))
#     # p2 = Process(target=dance, name = "p2",kwargs={"name": "bingbing"})
#     # # p1的子进程名是： p1
#     # # p2的子进程名是： p2
#
#     # 若子进程只是简单的创建和开始，程序会优先执行主进程程序
#     # 开始进程
#     p1.start()
#
#     # 主进程等待子进程
#     p1.join()
#
#     p2.start()
#
#     # 主进程等待子进程
#     p2.join()
#
#     '''修改子进程的名称：第二种方法'''
#     # p1.name = "pro1"
#     # p2.name = "pro2"
#     # # p1的子进程名是： pro1
#     # # p2的子进程名是： pro2
#
#     # 访问name属性；子进程对象名.name
#     print("p1的子进程名是：",p1.name)
#     print("p2的子进程名是：",p2.name)
#
#     # 访问子进程的进程编号
#     print("p1子进程编号：",p1.pid)
#     print("p2子进程编号：",p2.pid)
#
#      # 查看主进程进程编号
#     print(f"主进程ID：{os.getpid()}, 父进程ID:{os.getppid()}")
#
#     # 检查子进程是否仍然在运行
#     print("检查p1的存活状态：", p1.is_alive())
#     print("检查p2的存活状态：", p2.is_alive())

"""
未使用join(),主进程优先，子进程存活状态为Ture
使用join()，阻碍主程序，优先子程序（p1.join()）,子进程存活状态为False
"""

'''
线程共享资源；进程不共享资源
'''
# # 定义全局变量
# li = []
#
# #写入数据任务
# def write_data():
#     for i in range(5):
#         li.append(i)
#         time.sleep(i)  # 暂停一秒 import time
#     print("写入的数据：", li)
#
# # 读取数据任务
# def read_data():
#     print("读取的数据", li)
#
# # 主程序入口
# if __name__ == "__main__":
#     # 创建子线程
#     t1 = Process(target=write_data)
#     t2 = Process(target=read_data)
#
#     # 开始子进程
#     t1.start()
#     # 等待子进程执行
#     t1.join()
#
#     t2.start()

'''
（1）进程之间：
 未加入join():
     读取的数据 []
     写入的数据： [0, 1, 2, 3, 4]

 加入join:
    写入的数据： [0, 1, 2, 3, 4]
    读取的数据 []
    
进程之间，资源不共享，不存在竞争

（2）线程之间：
 未加入join():
     读取的数据 []
     写入的数据： [0, 1, 2, 3, 4]

 加入join:
    写入的数据： [0, 1, 2, 3, 4]
    读取的数据 [0, 1, 2, 3, 4]
    
线程之间，资源共享，存在竞争关系

    '''
'''线程资源共享，导致资源竞争的实例'''
# from threading import Thread
# # 定义全局变量
# li = []
#
# #写入数据任务
# def write_data():
#     for i in range(5):
#         li.append(i)
#         time.sleep(i)  # 暂停一秒 import time
#     print("写入的数据：", li)
#
# # 读取数据任务
# def read_data():
#     print("读取的数据", li)
#
# # 主程序入口
# if __name__ == "__main__":
#     # 创建子线程
#     t1 = Thread(target=write_data)
#     t2 = Thread(target=read_data)
#
#     # 开始子进程
#     t1.start()
#     # 等待子进程执行
#     # t1.join()
#
#     t2.start()

'''3.进程间的通信'''
'''
进程间的通信
    由于进程之间默认不直接共享资源，当他们需要访问或操作相同的数据或资源时，
就需要借助进程间通信机制来传递信息或数据，从而实现资源的共享与协调使用。

    multiprocessing，模块中Queue类是一个功能强大且易于使用的工具，它专为
多进程环境而设计，能够实现进程间数据的安全传递。
其常见的方法：
1.put():放入数据（入队）
2.get():取出数据（出队）       （一步一取）
3.empty():判断·队列是否为空。如果为空，则返回Ture,否则返回False.
4.qsize():返回当前队列包换的消息数量
5.full():判断队列是否已满。如果已满，返回True,否则返回False。

注：这里是存取，并非写读

队列（queue）不可遍历



'''
# # 实例化队列对象
# q = Queue(3)  # 最多队列可接受三条信息，如果没写或是负值则代表没有上限
#
# # 放入数据
# q.put("今晚平安夜")
# q.put("要回家吃苹果")
#
# # 判断队列是否已满
# print("判断队列是否已满",q.full())
#
# q.put("好开心")
#
# # 查看数据数量
# print("查看数据数量",q.qsize())
#
# # 判断队列是否已满
# print("判断队列是否已满",q.full())
#
# # 取出数据（一步一取）
# print(q.get())
# print(q.get())
#
# # 判断队列是否为空
# # print(q.empty())    # Ture放入的数据，已经取出，队列（queue）为空
# print(q.empty())    # False 取出两个，还剩一个，队列（queue1）不为空
#
#
# q.get()
# print(q.empty())  # Ture
#
# # 查看数据数量
# print(q.qsize())

# # 定义全局变量
# li = ["张三", "李四", "王五", "赵六"]
#
# # 写入数据任务
# def write_data(q):
#     # 将列表中的对象依次放入队列中
#     for i in li:
#         print(f"{i}已经放入队列中")
#         q.put(i)
#         time.sleep(0.2)
#
#
# # 读取数据任务
# def read_data(q):
#          # 只要队列中有消息就取出
#         while True:
#             # 判断队列是否为空
#             if q.empty():
#                 break
#             # 不为空取出
#             else:
#                 print(f"从队列中取出", q.get())
#
#
# # 主程序入口
# if __name__ == "__main__":
#     # 创建队列对象
#     q = Queue()
#     # 创建子进程
#     t1 = Process(target=write_data, args=(q,))
#     t2 = Process(target=read_data, args=(q,))
#
#     # 开始子进程
#     t1.start()
#
#     # 等待队列中的数据放入完成
#     t1.join()
#     t2.start()

"""4.进程池"""
'''
4.1 进程池 from multiprocessing into pool
    进程池可以被形象地比作一个水池，其中的“水盘”代表进程。在这个水池中，我们
可以设定“水盘”的数量，即限制同时运行的进程数，从而确定能并行处理的最大任务数量
    具体而言，进程池会预先创建并维护一定数量的进程。当有任务需求时，进程池会
分配一个空闲的进程来处理该任务。任务完成后，进程不会立即关闭，而是回到进程池中
继续等待新的任务分批。这种方式显著提高了资源利用率和任务处理效率。

4.2 常用方法
1.apply_async():异步非阻塞执行任务。这意味着主程序不会等待当前任务执行完成，
而是根据系统调度来进行行程切换，从而可以处理其他任务或继续执行主程序的其他代码。
注：如果使用异步提交任务，并且需要收集结果，应使用 get 方法来获取。get 方法
会阻塞，直到结果可用。

2.close():关闭进程池，使其不再接受新的任务。已经提交的任务会继续执行，但新的
任务将无法提交到进程池中。（单方面封锁：只出不进）

3.join():阻塞主进程，直到进程池中的所有工作进程都退出。这通常用于等待所有任
务都完成后再继续执行主程序的后续代码。

注：join方法必须在close()方法之后调用，否则可能引发异常或导致未定义行为。


'''
# 任务
def task(num):
    print("圣诞节快到了，还在执行任务~")
    time.sleep(2)
    return num*3

# 主程序入口
if __name__ == '__main__':
    # 实例化一个进程池对象，限制最大进程数3
    p = Pool(3)

    # 定义一个空列表
    li = []

    # 循环
    for i in range(7):
        # 执行：apply_async(target, 参数（实参 ）)
        # 异步：进程不需要一直等下去，而是继续执行下面的操作，不管其他进程的状态
        # 原来是顺序循环，但加入异步执行，即三个进程同时进行，按照原来的顺序，分步循环
        res = p.apply_async(task, args=(i,))
        # 赋值的是task的返回值，参数i是实参（变量），对应于形参num
        print(res)
        # 将返回数值结果放到新列表中
        li.append(res)


    # 关闭进程池
    p.close()

    # 等待进程池所有子进程进行完毕，必须放在close 后面
    p.join()

    # 使用get方法来获取apply_async()的结果
    for i in li:
        print(i.get())


