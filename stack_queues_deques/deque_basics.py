#!/usr/local/bin/python3
## DEQUE, Both ends

## methods/atrributes:
# Deque()
# isEmpty()
# size()
# addFront()
# addRear()
# removeFront()
# removeRear()

class Deque(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def addFront(self,item):
        return self.items.append(item)
    def addRear(self,item):
        return self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)

d = Deque()
d.addFront("Hello")
d.addRear("World")
print(d.size())
print(f"{d.removeFront()} {d.removeRear()}")
print(d.size())