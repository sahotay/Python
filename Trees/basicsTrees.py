#!/usr/local/bin/python3
###
# Tree Data Structure has root, branches and leaves
# All children of one node are independent of childer on another node
# each leaf node is unique

## File System, directories and folders are structure as trees
## Webpage are also an example of trees
###

myTree = ['a', #root 
        ['b', #Left Subtree
            ['d', [], []],
            ['e', [], []] ],
        ['c', #right subtree
            ['f', [], []],
        []]
        ]

## Trees Implementation using Lists
def BinaryTree(r):
    return [r, [], []]
def insertLeft(root,newBranch):
    t = root.pop()
    if len(t) > 1:
        root.insert(1, [newBranch,t,[]])
    else:
        root.insert(1, [newBranch,[],[]])
    return root
def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch,[],t])
    else:
        root.insert(2, [newBranch,[],[]])
    return root
def getRootVal(root):
    return root[0]
def setRootVal(root, newval):
    root[0] = newval
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]

r = BinaryTree(3)
print(insertLeft(r,4))
print(insertRight(r,6))
print(getRootVal(r))
print(getLeftChild(r))
print(getRightChild(r))


