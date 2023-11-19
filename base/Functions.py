# 测试基本的方法
def print_hello(name):
    print("hello python" + name)


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "The numbers are equal"
    else:
        return y


# 对于传入方法的参数进行类型转换
def print_max(x, y):
    x = int(x)
    y = int(y)
    if x > y:
        print("x is max")
    else:
        print("y is max")



