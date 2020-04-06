#!/usr/local/bin/python3

### 
# Tree Traversal
# 1. preorder,  root node -> left subtree -> right subtree
# 2. inorder, left subtree -> root node -> right subtree
# 3. postorder, left subtree -> right subtree -> root node 
###


class BinaryTree(object):
    def __init__(self, rootobject):
        self.key = rootobject
        self.leftchild = None
        self.rightchild = None
    def insertLeft(self, newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t
    def insertRight(self, newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t
    def getRightChild(self):
        return self.rightchild
    def getLeftchild(self):
        return self.leftchild
    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(r.getRootVal())
r.insertLeft('b')
print(r.getLeftchild().getRootVal())
r.insertLeft('e')
print(r.getLeftchild().getRootVal())
r.insertRight('c')
print(r.getRightChild().getRootVal())

def preOder(self):
    print(self.key)
    if self.leftchild:
        self.leftchild.preOder()
    if self.rightchild:
        self.rightchild.preOder()

def postOder(tree):
    if tree != None:
        postOder(tree.getLeftchild())
        postOder(tree.getRightChild())
        print(tree.getRootVal())

def inOder(tree):
    if tree != None:
        postOder(tree.getLeftchild())
        print(tree.getRootVal())
        postOder(tree.getRightChild())
        