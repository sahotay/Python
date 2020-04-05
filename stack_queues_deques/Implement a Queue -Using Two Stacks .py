#!/usr/local/bin/python3
'''
Implement a Queue - Using Two Stacks
Given the Stack class below, implement a Queue class using two stacks! Note, this is a "classic" interview problem. Use a Python list data structure as your Stack.
'''


class Queue2Stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []
    def enqueue(self, item):
        self.instack.append(item)
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                # Add the elements to the outstack to reverse the order when called
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())