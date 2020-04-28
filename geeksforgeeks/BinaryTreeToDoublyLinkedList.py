#!/usr/local/bin/python3
# Python3 program to convert a given Binary 
# Tree to Doubly Linked List 

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

class BinaryTree: 
	root, head = None, None
	
	# A simple recursive function to convert a given 
	# Binary tree to Doubly Linked List 
	def BToDll(self, root: Node): 
		if root is None: 
			return

		# Recursively convert right subtree 
		self.BToDll(root.right) 

		# Insert root into doubly linked list 
		root.right = self.head 

		# Change left pointer of previous head 
		if self.head is not None: 
			self.head.left = root 

		# Change head of doubly linked list 
		self.head = root 

		# Recursively convert left subtree 
		self.BToDll(root.left) 

	@staticmethod
	def print_list(head: Node): 
		print('Extracted Double Linked list is:') 
		while head is not None: 
			print(head.data, end = ' ') 
			head = head.right 

# Driver Code 
if __name__ == '__main__': 
	
	""" 
	Constructing below tree 
			5 
		// \\ 
		3 6 
		// \\ \\ 
		1 4 8 
	// \\ // \\ 
	0 2 7 9 
	"""
	tree = BinaryTree() 
	tree.root = Node(5) 
	tree.root.left = Node(3) 
	tree.root.right = Node(6) 
	tree.root.left.left = Node(1) 
	tree.root.left.right = Node(4) 
	tree.root.right.right = Node(8) 
	tree.root.left.left.left = Node(0) 
	tree.root.left.left.right = Node(2) 
	tree.root.right.right.left = Node(7) 
	tree.root.right.right.right = Node(9) 

	tree.BToDll(tree.root) 
	tree.print_list(tree.head) 


