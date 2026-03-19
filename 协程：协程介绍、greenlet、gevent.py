"""协程：协程介绍、greenlet、gevent"""
from greenlet import greenlet
import time
import gevent
from gevent import monkey
"""
1.协程的介绍
协程（Coroutine）：又称维线程或纤程,是python中一种轻量级的多任务实现方式。
相比于线程，协程的执行单位更小，资源占用更低，因为他不需要像线程那样创建独立的
内存空间和系统资源。协程自带cpu上下切换的功能，允许开发者在适当的时候，灵活地
在不同协程间进行切换。在切换过程中，通过保存和恢复cpu上下文，程序能够持续保持
其运行状态，从而1确保多任务的连续性和高效性。

简单来说，协程允许在单个线程内的函数执行过程中，随时保存当前函数的执行状态
（包括临时变量等信息），并切换到另一个函数继续执行，这种切换并非通过函数调用
实现，而是开发者根据实际需求，自主决定切换的时机和次数。

 注：线程与进程的操作通常需要程序调用系统接口，并有操作系统负责最终的执行；而
 协程的调度与执行则完全由程序员掌控，无需依赖操作系统的介入。

 应用场景：
1.如果一个线程里面IO操作（网络请求、文件较多），协程就比较适用
2.适合用于高并处理

"""

"""
简单实现协程
注：生成器函数可以被用来简洁地实现协程的基本功能，
即实现一个函数到另一个函数的灵活切换
生成器函数：函数中包含yeild关键字
"""
# # 生成器函数：函数中包含yeild关键字
# def task1():
#     while True:
#         yield 123
#  # yield作用：返回123，并暂停函数，在此处挂起，使用next()再次调用生成器时，再从此处恢复执行
#         yield "shuohua"
#
# def task2():
#     while True:
#         yield 456
#         yield "huahua"
#
# # 主程序入口
# if __name__ == '__main__':
#     # 调用函数
#     t1 = task1()    # 调用生成器函数
#     # print(t1)       # 返回生成器函数对象
#     t2 = task2()
#
#     # # 获取值
#     # print(next(t1))
#     # print(next(t2))
#     # print(next(t1))
#     # print(next(t2))
#
#     # for i in range(2):
#     #      print(next(t1))
#     #      print(next(t2))
#
#
#     while True:
#
#          print(next(t1))
#          print(next(t2))

"""2.greenlet"""
'''
greenlet是一个第三方库，它提供了一种轻量级的协程实现。通过switch方法，它能够在
在不同的执行路径（或称为协程，greenlet）之间进行手动切换。然而，需要注意的是，
由于这种切换时手动的，所以当某一个协程遇到IO操作时，如果没有额外的机制来处理，
程序将会在该处阻塞，并不会自动切换到其他行程

安装命令：pip install greenlet 

1.导入模块 from greenlet import greenlet
2.实例化对象  p1 =greenlet（）
3.调用执行（切换执行） p1.switch()

注：若使用swith在函数中，调用函数，执行到切换命令（p1.switch），此命令后面
的代码不执行

greenlet 工作流程为：开发者需要通过手动通过 switch 方法在不同的执行路径
（协程或greenlet）之间进行切换。当某个greenlet遇到阻塞的I/O操作时，如果
没有其他机制来主动处理这种阻塞，那么该greenlet的执行将暂停，导致程序在该处
停滞。然而，greenlet框架允许我们切换到另一个当前未被阻塞的greenlet继续执行，
一旦原先阻塞的greenlet的阻塞状态被解除（例如网络请求完成），开发者可以手动
调用switch方法切换回原来的greenlet,从阻塞点之后继续执行剩余的代码。

'''
from greenlet import greenlet
# # 唱歌任务
# def sing():
#     print("在唱歌")
#     p2.switch()  # 唱完歌了没有执行，切换到p2中执行
#     print("唱完歌了")
#
#
#
# def dance():
#     print("在跳舞")
#     p1.switch()  # 跳完舞了没有执行
#     print("跳完舞了")
#     # p1.switch()
#
# # sing()
# # dance()
#
# # 主程序入口
# if __name__ == '__main__':
#     # 实例化协程对象：greenlet（任务名）
#     p1 = greenlet(sing)
#     p2 = greenlet(dance)
#
#     p1.switch()  # 切换到p1中运行
#     # p2.switch()  # 切换到p2中运行

"""3.gevent"""
'''
gevent
greenlet虽然实现了协程的基本概念，但需要开发者手动通过switch方法在不同的
执行路径之间进行切换，这在一定程度上增加了开发的复杂性和工作量。为了解决这个
问题，gevent这一功能更为强大且能够自动切换任务的第三方库应运而生。

在gevent中，当遇到I/O操作时，它回自动进行主动式任务切换，
而greenlet则是实现这一功能的主要协程模式。

在使用gevent之前，同样需要通过pip命令来安装它，具体安装命令为
            pipi install gevent


常用方法
1.spawn():创建一个新的协程对象，并立即开始执行传入的函数
2.sleep():执行一个耗时操作，即让当前协程暂停，执行执行指定的秒数
        多个sleep()，同时执行暂停，实现并发效果边跳边唱（非time,sleep）
3.join():阻塞当前协程，直到执行的协程对象执行完毕
4.joinall():等待传入的协程对象队列中所有协程都执行完毕
                gevent.joinall([g1, g2])
                
给程序打补丁
    在之前的gevent协程实现中，我们使用了gevent.sleep（）来代替time.sleep()
以模拟等待，这是因为gevent需要通过其内部实现的模块来处理耗时操作，从而实现协程
之间的自动切换。
    然而，在实际开发中，代码往往更复杂，直接修改代码并不总是可行的，为了解决
这个问题，gevent提供了一个强大的monkey补丁功能，该功能能够在程序运行时动态
地替换模块中的函数或方法，聪儿将耗时代码自动转换为gevent的实现，而无需修改
原代码

         from gevent import monkey
                
'''

import gevent
# import time
# def sing():
#     print("在唱歌")
#     gevent.sleep(2)  # 模拟的是gevent可以识别的IO阻塞
#     print("唱完歌了")
#
#
#
# def dance():
#     print("在跳舞")
#     gevent.sleep(1)
#     print("跳完舞了")
#
# # 主程序入口
# if __name__ == '__main__':
#     # 创建协程对象（类似于greenlet(模版导入不同，会有差别)）
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#
#     # 阻塞方法：等待协程执行完毕
#     g1.join()   # 等待g1对象执行结束
#     g2.join()   # 等待g2对象执行结束

monkey.patch_all() # 将用到的time.sleep()替换为gevent,sleep
# 注：monkey.path_all()必须放在被打补丁之前

def sing(name):
    for i in range(1, 4):
        # gevent.sleep(1)
        time.sleep(1)
        print(f"{name}在唱歌，被送走的第{i}次")

# 主程序入口
if __name__ == '__main__':
    # 等待所有的协程对象都执行完毕
    gevent.joinall([ gevent.spawn(sing, "bingbing"),
   gevent.spawn(sing, "冰冰")])
    # #创建协程
    # g1 = gevent.spawn(sing, "bingbing")
    # g2 = gevent.spawn(sing, "冰冰")

# 注：如果没有遇到可识别的IO操作，不会进行任务切换，实现并发效果




