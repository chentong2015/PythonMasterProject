#!/usr/bin/env python

class BaseClass(object):
    def __init__(self):
        self.name = "base class"

    def feature1(self):
        print("This is feature1 {}".format(self.name))


# TODO. 定义类型时，()中指定的是该类型的父类
# 子类会自动继承父类所定义好的代码，并补充新的逻辑
# 子类只能继承父类的非私有属性和非私有的方法
class SubClass(BaseClass):
    def __init__(self):
        # 先调用父类的构造进行初始化
        super().__init__()
        self.name = "sub class"

    def feature2(self):
        print("This is feature2 {}".format(self.name))


def get_class(type):
    if type == "base":
        return BaseClass()
    elif type == "sub":
        return SubClass()
    else:
        print("Can't find class type")
    return None


if __name__ == "__main__":
    base = get_class("base")
    base.feature1()

    sub = get_class("sub")
    sub.feature1()
    sub.feature2()