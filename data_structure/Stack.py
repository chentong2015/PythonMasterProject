#!/usr/bin/env python

# TODO. 使用list数组加index来实现stack栈的逻辑功能
class Stack(object):
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top_index = -1

    # 入栈之前检查栈是否已满
    def push(self, x):
        if self.is_full():
            print("stack is full")
        else:
            self.stack.append(x)
            self.top_index = self.top_index + 1

    # 出栈之前检查栈是否为空
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            self.top_index = self.top_index - 1
            self.stack.pop()

    def is_full(self):
        return self.top_index + 1 == self.size

    def is_empty(self):
        return self.top_index == '-1'

    def show_stack(self):
        print(self.stack)


if __name__ == '__main__':
    s = Stack(10)
    for i in range(6):
        s.push(i)

    s.show_stack()
    for i in range(3):
        s.pop()
    s.show_stack()
