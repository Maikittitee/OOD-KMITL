from example import BST, Node

class AVL():
	class AVLNode:
		def __init__ (self, data, left = None, right = None):
			self.data = data
			self.left = left
			self.right = right
			self.height = self.set_height()

		def __str__(self):
			return (f"{self.data}/{self.height}")

		def set_height(self):
			l_node = self.get_height(self.left)
			r_node = self.get_height(self.right)
			self.height = 1 + max(l_node, r_node)
			return (self.height)
		
		def get_height(self, node):
			return -1 if node == None else self.height
		
		def insert(node, new_data) -> "AVL.AVLNode":
			if (node == None):
				print("here")
				return AVL.AVLNode(new_data)
			if (new_data < node.data):
				node.left = AVL.AVLNode.insert(node.left, new_data)
			else:
				node.right = AVL.AVLNode.insert(node.right, new_data)
			node = AVL.rebalance(node)
			node.height = node.set_height()
			return (node)

		def side_print(node, deep = 0):
			if (node == None):
				return
			AVL.AVLNode.side_print(node.right, deep + 1)
			print("\t" * deep, end = "")
			print(node)	
			AVL.AVLNode.side_print(node.left, deep + 1)

		def balance_factor(self):
			return (self.get_height(self.left) - self.get_height(self.right))

	def __init__ (self):
		self.root = None

	def rebalance(node : "AVL.AVLNode"):
		bf = node.balance_factor()
		if (bf == -2):
			if (node.right.balance_factor() == 1):
				node.left = AVL.rotate_right(node.left)
			node = AVL.rotate_left(node)
		elif (bf == 2):
			if (node.right.balance_factor() == -1):
				node.right = AVL.rotate_left(node.right)
			node = AVL.rotate_right(node)
		# node.height = node.set_height()
		return (node)

	def insert(self, new_data):
		self.root = AVL.AVLNode.insert(self.root, new_data)
		return (self.root)
	
	def rotate_left(node:"AVL.AVLNode"):
		A = node
		B = node.right
		A.right = B.left
		B.left = A
		A = B
		A.left.height = A.left.set_height()
		A.height = A.set_height()
		return (A)


	def rotate_right(node:"AVL.AVLNode"):
		A = node
		B = A.left
		tmp = B.right
		B.right = A
		A.left = tmp
		A = B
		A.right.height = A.right.set_height()
		A.height = A.set_height()
		return (A)

	def side_print(self):
		self.AVLNode.side_print(self.root)
	
a = AVL()
a.insert(1)
a.insert(2)
a.insert(3)
print(f"a.root is {a.root}")
a.side_print()
# print("------")
# a.rebalance(a.root)
# a.root = a.rotate_right(a.root)
# a.side_print()

# a.root = a.rotate_left(a.root)
# print(f"a.root is {a.root.data}")
# a.side_print()