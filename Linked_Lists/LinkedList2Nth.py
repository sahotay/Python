#!/usr/local/bin/python3
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


def nth_to_lastNode(n, head):
    left_pointer = head
    right_pointer = head
    for i in range(n-1):
        if not right_pointer.next:
            raise LookupError("Error: n is larger than the linked list")
        right_pointer = right_pointer.next
    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
    return left_pointer

#### Test
from nose.tools import assert_equal
class TestNLast(object):
    def test(self,sol):
        assert_equal(sol(2,a),d)
        print("TEST CASE PASSED")
        
# Run tests
t = TestNLast()
t.test(nth_to_lastNode)