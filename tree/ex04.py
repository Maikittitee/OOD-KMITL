class Node:
	def __init__(self, data): 
		self.data = data  
		self.left = None  
		self.right = None 
		self.level = None 

	def __str__(self):
		return str(self.data)

	def insert(node, new_data) -> "Node":
		if (node == None):
			return Node(new_data)
		if (new_data < node.data):
			node.left = Node.insert(node.left, new_data)
		else:
			node.right = Node.insert(node.right, new_data)
		return (node)
			 

class BinarySearchTree:
	def __init__(self): 
		self.root = None

	def insert(self, val):
		self.root = Node.insert(self.root, val)

	def delete(self, r, data):
		pass
		#code here
				
def printTree90(node, level = 0):
	if node != None:
		printTree90(node.right, level + 1)
		print('     ' * level, node)
		printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
#code here