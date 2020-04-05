#!/usr/local/bin/python3
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a

def cycleCheck(node):
    # Edge case check
    if node.next is None:
        return False
    # Begin both markers at the first node
    marker1 = node
    marker2 = node
    # Go until end of list
    while marker2 != None and marker2.next != None:
        marker1 = marker1.next
        marker2 = marker2.next.next
        if marker2 == marker1:
            return True
    # Case where marker ahead reched end of the list
    return False

print(cycleCheck(a))