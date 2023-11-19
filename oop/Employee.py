#!/usr/bin/env python

class Employee(object):

    # 定义类型的构造器(default constructor 初始化器)
    # init方法第一个参数必须是self, 允许传递任意数量的参数
    # self is a reference to the current instance of the class
    def __init__(self, name, index, phone):
        self.name = name
        self.index = index
        self.phone = phone

    # TODO. 定义class方法的时候必须提供self参数，但是调用该方法时不需要提供self
    # Python pass self automatically
    def get_name(self):
        return self.name

    # Python会自动做GC
    # 不需要现实的删除或者释放对象


if __name__ == '__main__':
    # 直接创建新的对象并将引入传递给变量
    employee = Employee('tong', 10, "076")
    print(employee.get_name())
