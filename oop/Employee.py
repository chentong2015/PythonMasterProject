class Employee(object):

    # 定义类型的构造器(default constructor 初始化器)
    # init方法可以传递任意数量的参数，第一个参数必须是self
    def __init__(self, name, index, phone):
        self.name = name
        self.index = index
        self.phone = phone

    def get_name(self):
        return self.name


if __name__ == '__main__':
    employee = Employee('tong', 10, "076")
    print(employee.get_name())
