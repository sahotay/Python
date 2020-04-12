class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

def removeKFromList(l, k):
    # Edge case check
    if l == None:
        return l
    elif l.data == k:
        l = l.next
    current = l
    while current != None and current.next != None:
        if current.next.data == k:
            current.next = current.next.next
        else:
            current = current.next  
    
    if  current != None and current.data == k:
        l = l.next
    return l

NodeA = Node(3)
NodeB = Node(5)
NodeC = Node(2)
NodeD = Node(4)
NodeE = Node(1)
NodeA.next = NodeB
NodeB.next = NodeC
NodeC.next = NodeD
NodeD.next = NodeE

k =5
print(removeKFromList(NodeA,k))