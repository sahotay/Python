class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def isListPalindrome(l):
    temp = []
    while l is not None:
        temp.append(l.data)
        l = l.next

    return(temp == temp[::-1])

NodeA = Node(1)
NodeB = Node(0)
NodeC = Node(0)
NodeD = Node(0)
NodeE = Node(1)
NodeA.next = NodeB
NodeB.next = NodeC
NodeC.next = NodeD
NodeD.next = NodeE



print(isListPalindrome(NodeA))