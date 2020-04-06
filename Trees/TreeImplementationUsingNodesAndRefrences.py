#!/usr/local/bin/python3
## Trees Implementation using Nodes and Refrences 

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
r.insertRight('c')
print(r.getRightChild().getRootVal())