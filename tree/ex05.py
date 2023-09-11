#	ปริ้นต้นไม้ BST เป็นแนวนอน          ที่ครูสอนพี่ฟงนั้นขัดใจ
#	อยากให้น้องทำใหม่ช่วยแก้ไข        ให้ต้นไม้ตั้งตรงแตกกิ่งได้
#	เลขวรรคขั้นสำหรับข้อมูลรับ            แนะว่านับจำนวนให้ดีไว้
#	ทำออกมาให้สวยงามประทับใจ       กฤษฎาอยู่ในป่ายังเชยชม

#	*วนลูป insert เลขทีละตัวเข้า tree ตามปกติ < อยู่ซ้าย, >= อยู่ขวา

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

	def count_r_space(node):
		if (node == None):
			return (0)
		elif (node.data < 0):
			return (2 + Node.count_r_space(node.right))
		return (1 + Node.count_r_space(node.right))

	def count_l_space(node):
		if (node == None):
			return (0)
		elif (node.data < 0):
			return (2 + Node.count_l_space(node.left))
		return (1 + Node.count_l_space(node.left))


	def print_promax(node: "Node", root, nl = 1, deep = 0):
		if (node == None):
			return 
		print(' ' * Node.count_l_space(node.left), end = '')
		if (nl == 1):
			print(node.data)
		else:
			print(node.data, end = '')
		curr = root
		i = 0
		while (curr != None):
			if (i == deep):
				print(curr.deep,end = '')
			i += 1
		

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
		self.root = Node.insert(self.root, new_data)

	def print_promax(self):
		Node.print_promax(self.root)
	
	def print(self):
		Node.print(self.root)

t = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
	root = t.insert(i)
t.print_promax()

print("-----------------")
t.print()
	