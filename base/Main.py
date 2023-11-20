#!/usr/bin/python
# coding=utf-8

# 声明引入的类型，标记从什么模块中进行引入
# 类对引用的格式: from 包名.文件名 import 类名
import sys
from base import Functions


def test_data_types():
    # python 可以实现同步赋值
    x, y = 1, 2
    x, y = y, x
    print("x =", x)
    print("y =", y)
    a = 20
    b = 5.5
    c = True
    print(type(a), type(b), type(c))


def test_import_module():
    # 调用引入modules中定义的方法
    Functions.print_hello("python")
    print(Functions.maximum(10, 20))


# TODO. Python程序入口, 执行python文件时会执行该方法，并且执行文件中定义的可被执行的逻辑
if __name__ == '__main__':
    # input() 用于用户的标准输入，获取输入的值
    info = input()
    print("Your input: ", info)

    # This line print all the arguments of this scripts
    for arg in sys.argv:
        print("Arg =", arg)
