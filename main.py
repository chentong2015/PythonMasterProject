import functions

# 注意main主方法的间隔
if __name__ == '__main__':
    a = 20
    b = 5.5
    c = True
    print(type(a), type(b), type(c))
    single_q = 'this is a string'
    double_q = "this is a string"
    print(single_q, double_q)

    # 调用引入modules中定义的方法
    functions.print_hello("python")
    print(functions.maximum(10, 20))
