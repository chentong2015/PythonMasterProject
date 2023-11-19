# TODO. classmethod类方法，通过类名称进行调用的方法
# 类方法是给类用的，在使用时会将类本身(cls)当做参数传给类方法的第一个参数

class ClassTest(object):
    # 在类的内部首先定义私有变量，名称和初始值
    __num = 0

    # 新建实例对象时候调用的函数，统计类型被创建的数目
    def __new__(cls):
        ClassTest.add_num()
        return super(ClassTest, cls).__new__(cls)

    @classmethod
    def add_num(cls):
        cls.__num += 1

    @classmethod
    def get_num(cls):
        return cls.__num


class SubClassTest(ClassTest):
    def __init__(self):
        super().__init__()
        self.name = ''


if __name__ == "__main__":
    a = SubClassTest()
    b = SubClassTest()
    c = SubClassTest()
    d = SubClassTest()
    print(ClassTest.get_num())
