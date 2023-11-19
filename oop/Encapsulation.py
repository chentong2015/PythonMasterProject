#!/usr/bin/env python

class Encapsulation(object):
    # TODO. 使用不同的_变量标识来定义field的可访问性
    def __init__(self, pub, pro, pri):
        self.public = pub
        self._protected = pro
        self.__private = pri


class BankAccount(object):
    # 在初始化函数中定义的私有变量是不能通过外部直接访问到的，需要通过函数方法操作
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.__balance


if __name__ == '__main__':
    x = Encapsulation(11, 13, 17)
    print("Public: {}".format(x.public))
