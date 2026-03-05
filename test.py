name = "test"
def func():
    print("这是test模块中的fun函数")
def fund():
    print("这是test模块中的fund函数")

print("test模块中__name__的值",__name__)
if __name__ == '__main__':
    # 测试代码
    print("我的名字",name)
    func()
    fund()
