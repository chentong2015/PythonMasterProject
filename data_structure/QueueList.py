#!/usr/bin/env python

if __name__ == '__main__':
    # Initializing a queue
    queue = []

    # Adding elements to the queue
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print("Initial queue")
    print(queue)

    # Removing elements from the queue
    print("\n Elements dequeued from queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    print("\n Queue after removing elements")
    print(queue)


