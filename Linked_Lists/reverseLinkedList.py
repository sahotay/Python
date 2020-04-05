#!/usr/local/bin/python3
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    current = head
    previous = None
    next = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
print(a.data)
print(a.next.data)
print(b.next.data)
print(c.next.data)
reverse(a)
print(d.data)
print(d.next.data)
print(c.next.data)
print(b.next.data)