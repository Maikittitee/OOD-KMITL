class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = self.setHeight()

	def __str__(self):
		return str(self.data)
		
	def setHeight(self):
		return 1 + max(self.getHeight(self.left), self.getHeight(self.right))
	
	def getHeight(self, node):
		if node == None:
			return (0)
		else:
			return (node.height)
	
	def balanceValue(self):
		return self.getHeight(self.left) - self.getHeight(self.right)
	
	def rightRotate(self, x) :
		y = x.left
		x.left = y.right
		y.right = x
		x = y
		x.right.setHeight()
		x.setHeight()
		return x
	
	def leftRotate(self, x) :
		y = x.right
		x.right = y.left
		y.left = x    
		x = y
		x.left.setHeight()
		x.setHeight()
		return x
	
	def insert(node, data):
		if (node == None):
			return (Node(data))
		if (data < node.data):
			node.left = Node.insert(node.left, data)
		else:
			node.right = Node.insert(node.right, data)
		
		node.height = node.setHeight()
		balance = node.balanceValue()
		# print(f"balance of {node.data} is {balance}")
		if balance > 1 and data < node.left.data:
			return node.rightRotate(node)
 
		# Case 2 - Right Right
		if balance < -1 and data > node.right.data:
			return node.leftRotate(node)
 
		# Case 3 - Left Right
		if balance > 1 and data > node.left.data:
			node.left = node.leftRotate(node.left)
			return node.rightRotate(node)
 
		# Case 4 - Right Left
		if balance < -1 and data < node.right.data:
			node.right = node.rightRotate(node.right)
			return node.leftRotate(node)
 
		return node

class AVL:
	def __init__ (self):
		self.root = None

	def insert(self, data):
		self.root = Node.insert(self.root, data)

	def printTree(self, node, level = 0):
		if node != None:
			self.printTree(node.right, level + 1)
			print('     ' * level, node)
			self.printTree(node.left, level + 1)


t = AVL()

inp = list(map(int, input("Enter Input : ").split()))
for i in inp:
	print(f"Insert : ( {i} )")
	t.insert(i)
	t.printTree(t.root)
	# t.preOrder(t.root)
	print("--------------------------------------------------")
