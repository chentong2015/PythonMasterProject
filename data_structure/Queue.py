#!/usr/bin/env python

from queue import Queue


if __name__ == '__main__':
    queue = Queue()
    for i in range(5):
        queue.put(i)

    while not queue.empty():
        print("item = ", queue.get())

'''
# 队列：队列是FIFO的（先进先出）
class Queue():
    def _init_(qu, size):
        qu.queue = [];
        qu.size = size;
        qu.head = -1;
        qu.tail = -1;

    def Empty(qu):
        if qu.head == qu.tail:
            return True
        else:
            return False

    def Full(qu):
        if qu.tail + 1 - qu.head == qu.size:
            return True
        else:
            return False

    def enQuene(qu, content):
        if qu.Full():
            print "The queue is full"
        else:
            qu.tail = qu.tail + 1
            qu.queue.apprend(content)

    def outQueue(qu):
        if qu.Empty():
            print " The queue is empty"
        else:
            qu.head = qu.head + 1
            return qu.queue[qu.head]

'''
