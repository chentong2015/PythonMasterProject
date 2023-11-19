# TODO. 静态方法: 静态方法用于提供除了__init__函数以为的方式来创建实例

# import the module timer
import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 用Date.now()的形式去产生实例,该实例用的是当前时间
    @staticmethod
    def now():
        t = time.localtime()  # 获取结构化的时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


if __name__ == "__main__":
    a = Date('1987', 11, 27)  # 自定义时间
    b = Date.now()  # 采用当前时间
    c = Date.tomorrow()  # 采用明天的时间

    print(a.year, a.month, a.day)
    print(b.year, b.month, b.day)
    print(c.year, c.month, c.day)
