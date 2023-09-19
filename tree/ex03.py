class Node:
	def __init__ (self, data):
		self.data = data
		self.left = None
		self.right = None
	
			
	# def insert_promax(node, new, target):
	# 	node.left = Node.insert_promax(node.left, new)

	def inorder(node):
		if (node == None):
			return
		Node.inorder(node.left)
		print(node.data)
		Node.inorder(node.right)


class BST:
	def __init__ (self):
		self.root = None
	
	def insert(self, new_data, target_node_data = None):
		self.root = Node.insert(self.root, new_data, target_node_data)
		
	def inorder(self):
		Node.inorder(self.root)	

t = BST()

first = True
inp = input("Enter Input : ").split(',')
for i in inp:
	target, new = i.split()
	if (first == True):
	t.insert(new, target)

t.inorder()

