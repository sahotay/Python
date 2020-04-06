#!/usr/local/bin/python3
import collections
class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print (currentNode.data)
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if currentCount == 0:
            print("\n")
            currentCount,nextCount = nextCount,currentCount


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left = Node(6)
root.right = Node(7)
root.left = Node(8)
root.right = Node(9)

levelOrderPrint(root)
