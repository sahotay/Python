#!/usr/local/bin/python3
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
    
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
print(a.data)
print(a.next.data)