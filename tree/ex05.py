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


	def print_promax(node):
		"""Returns list of strings, width, height, and horizontal coordinate of the root."""
		# No child.
		if node.right is None and node.left is None:
			line = '%s' % node.data
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# Only left child.
		if node.right is None:
			lines, n, p, x = node.left.print_promax()
			s = '%s' % node.data
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# Only right child.
		if node.left is None:
			lines, n, p, x = node.right.print_promax()
			s = '%s' % node.data
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# Two children.
		left, n, p, x = node.left.print_promax()
		right, m, q, y = node.right.print_promax()
		s = '%s' % node.data
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2

	
	

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
		return (Node.print_promax(self.root))

	def print_promax_ultra(self):
		lines, a, b, c = self.print_promax()
		for line in lines:
			print(line)

	def print(self):
		Node.print(self.root)

t = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
	root = t.insert(i)
t.print_promax_ultra()

# print("-----------------")
# t.print()
	