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
	

	def print(node, deep = 0):
		if (node == None):
			return
		Node.print(node.right, deep + 1)
		print(f"{'     ' * deep}{node.data}")
		Node.print(node.left, deep + 1)

	def gen_str(node, str_list:list = []) -> "tuple[str, int, int, int]":
		if (node == None):
			return [], 0, 0, 0
		
		# get data of its child
		left, l_of_l, len_of_l, r_of_l = Node.gen_str(node.left)
		right, l_of_r, len_of_r, r_of_r = Node.gen_str(node.right)

		# join for str of its child
		str_list.insert(0, str(' ' * (l_of_l + len_of_l + r_of_l + 1)) + left.pop() + str(' ' * len(str(node.data))) + right.pop + str(' ' * (r_of_r + len_of_r + l_of_r + 1)))
		


#   6
#  / \
# 5   10
		pass


		

class BST:
	def __init__(self):
		self.root = None

	def insert(self, new_data):
		self.root = Node.insert(self.root, new_data)

	def print_promax(self):
		s = Node.gen_str(self.root)
		for i in s:
			print(i)


	def print(self):
		Node.print(self.root)

	def __str__(self) -> str:
		lines = BST.print_promax(self.root, 0, False, "-")[0]
		return "\n".join((line.rstrip() for line in lines))

t = BST()
inp = [int(i) for i in input('Enter input: ').split()]
for i in inp:
	root = t.insert(i)
t.print_promax()
# print(t, end = '')

# print("-----------------")
# t.print()
	