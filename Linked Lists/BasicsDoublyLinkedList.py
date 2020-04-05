#!/usr/local/bin/python3
# header node at the beginning of the list
# Tailer node at the end of the list
# "Dummy" nodes are known as sentinels (or guards)

class DoublyLinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode("five")
a.next = b
b.prev = a
b.next = c
c.prev = b
print(a.data)
print(a.next.data)
print(b.next.data)
#Reverse
print(c.prev.data)
print(b.prev.data)

