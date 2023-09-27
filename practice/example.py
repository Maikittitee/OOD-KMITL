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

	def traverse_bfs(q: list["Node"], l:list = []):
		if (len(q) == 0):
			return (l)
		curr = q.pop(0)
		l.append(curr.data)
		if (curr.left):
			q.append(curr.left)
		if (curr.right):
			q.append(curr.right)
		return (Node.traverse_bfs(q, l))


class BST:
	def __init__(self):
		self.root = None

	def insert(self, new_data):
		self.root = Node.insert(self.root, new_data)
		
	def inorder(self):
		Node.inorder(self.root)
	
	def preorder(self):
		Node.preorder(self.root)

	def postorder(self):
		Node.postorder(self.root)
	
	def print(self):
		Node.print(self.root)

	def BFS_iter(self : "BST"): 
		# column matter
		q = []
		ret = []
		q.append(self.root)
		while (len(q) > 0):
			curr = q.pop(0)
			ret.append(curr.data)
			if (curr.left):
				q.append(curr.left)
			if (curr.right):
				q.append(curr.right)
		return (ret)

	def BFS_recur(self):
		q = [self.root]
		return (Node.traverse_bfs(q))


import sys

t = BST()
if (len(sys.argv) == 1):
	l = [5,2,7,1,4,6,3]
else:
	l = sys.argv[1:]

for i in l:
	t.insert(i)
print(f"iterative: {t.bfs_iter()}")
print(f"recursive: {t.bfs_recur()}")

