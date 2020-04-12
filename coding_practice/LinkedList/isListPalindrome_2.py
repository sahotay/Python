#!/usr/local/bin/python3
# Node class
class Node(object):
    def __init__(self,data):
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 

# Linked List class contains a Node object 
class LinkedList(object):
    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    
    def get_prev_node(self, ref_node):
        current = self.head
        while(current and current.next!=ref_node):
            current = current.next
        return current
    
    def printList(self): 
        current = self.head 
        while (current):
            print(current.data)
            current = current.next

def is_palindrome(llist):
    start = llist.head
    end = llist.last_node
    while (start != end and end.next != start):
        if start.data != end.data:
            return False
        start = start.next
        end = llist.get_prev_node(end)
    return True

def main():
    a_llist = LinkedList()
    data_list = input("Enter Linked List elements: ").split()
    for data in data_list:
        a_llist.append(int(data))
    a_llist.printList() # Print Linked List
    if is_palindrome(a_llist):
        print('This is a palindromic list')
    else:
        print('This is non palindromic')

if __name__ == '__main__':
    main()