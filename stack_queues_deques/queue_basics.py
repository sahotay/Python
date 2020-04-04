#!/usr/local/bin/python3
## QUEUE, FIFO
### operations/Attributes are: Queue(), enqueue(item), dequeue(), isEmpty(), size()

class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()