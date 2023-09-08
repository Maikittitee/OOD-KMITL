class Node:
	def __init__(self, data):
		self.data = data
		self.left: "Node" = None
		self.right: "Node" = None

	def insert(node, new_data) -> "Node":
		if (node == None):
			return Node(new_data)
		if (new_data < node.data):
			node.left = Node.insert(node.left, new_data)
		else:
			node.right = Node.insert(node.right, new_data)
		return (node)
			
		
	def inorder(node):
		if (node == None):
			return
		Node.inorder(node.left)
		print(node.data)
		Node.inorder(node.right)

	def preorder(node):
		if (node == None):
			return
		print(node.data)
		Node.preorder(node.left)
		Node.preorder(node.right)

	def postorder(node):
		if (node == None):
			return
		Node.postorder(node.left)
		Node.postorder(node.right)
		print(node.data)

	def print(node, deep = 0):
		if (node == None):
			return
		Node.print(node.right, deep + 1)
		print(f"{'     ' * deep}{node.data}")
		Node.print(node.left, deep + 1)

class BST:
	def __init__(self):
		self.root = None

	def insert(self, new_data):
		new_node = Node(new_data)
		if (not self.root):
			self.root = new_node
		else:
			curr = self.root
			while (curr != None):
				if (new_data < curr.data):
					if (curr.left == None):
						curr.left = new_node
						return 
					curr = curr.left
				else:
					if (curr.right == None):
						curr.right = new_node
						return 
					curr = curr.right
		
	def inorder(self):
		Node.inorder(self.root)
	
	def preorder(self):
		Node.preorder(self.root)

	def postorder(self):
		Node.postorder(self.root)
	
	def print(self):
		Node.print(self.root)

t = BST()
l = [5,2,7,1,4,6,3]
for i in l:
	t.insert(i)
t.print()
# a = None
# a = Node.insert(a, 1)

'''
	7	
		6
5
		4
			3
	2
		1

'''