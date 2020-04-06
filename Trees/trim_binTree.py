#!/usr/local/bin/python3
#       8
#      / \
#    3    10
#   /\      \
#  1  6      14


class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def trimBST(tree, minVal, maxVal):
    if not tree:
        return
    tree.left = trimBST(tree.left,minVal,maxVal)
    tree.right = trimBST(tree.right,minVal,maxVal)

    if minVal <= tree.data <= maxVal:
        return tree
    if tree.data < minVal:
        return tree.right
    if tree.data > maxVal:
        return tree.left

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left = Node(1)
root.right = Node(6)


print(trimBST(root, 5, 8))
