class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def __str__(self):
		if self.isEmpty():
			return "Empty"
		cur, s = self.head, str(self.head.value) + " "
		while cur.next != None:
			s += str(cur.next.value) + " "
			cur = cur.next
		return s

	def isEmpty(self):
		return self.head == None

	def append(self, item):
		new_node = Node(item)
		if (self.isEmpty()):
			self.head = new_node
		else:
			curr = self.head
			while (curr.next):
				curr = curr.next
			curr.next = new_node

	def addHead(self, item):
		new_node = Node(item)
		if (self.isEmpty()):
			self.head = new_node
		else:
			new_node.next,self.head = self.head,new_node
			# self.head = new_node

	def search(self, item):
		curr = self.head
		while (curr and curr.value != item):
			curr = curr.next
		if (not curr):
			return (f"Not Found {item}")
		return (f"Found {item}")

	def index(self, item):
		curr,cnt = self.head,0
		while (curr and curr.value != item):
			curr = curr.next
			cnt += 1
		if (not curr):
			return (-1)
		return (cnt)	
		# Code Here

	def size(self):
		if (self.isEmpty()):
			return (0)
		curr,cnt = self.head,0
		while (curr):
			curr = curr.next
			cnt += 1
		return (cnt)
		# Code Here

	def pop(self, pos):
		curr, i = self.head, 0
		if (self.isEmpty()):
			return ("Out of Range")
		if (pos == 0):
			self.head = curr.next
			return ("Success")
		while(curr.next):
			if (i == pos - 1):
				curr.next = curr.next.next
				return ("Success")
			i += 1
			curr = curr.next
		return ("Out of Range")
		# Code Here
	def __contains__(self, value):
		if self.isEmpty():
			return False
		cur = self.head
		while (cur != None):
			cur = cur.next
			if (cur.value == value):
				return True
		return False

def	join_node(inp, checker):
	for i in inp:
		ele = i.split('>')
		first = int(ele[0])
		sec = int(ele[1])
		checker.get(first).next = checker.get(sec)

def	get_heads(inp, checker):
	head_checker = dict()
	pointed_checker = dict()
	ret_list = []
	for i in inp:
		ele = i.split('>')
		first = int(ele[0])
		sec = int(ele[1])
		print(f"when {i} ---")
		if (head_checker.get(first) == None):
			head_checker[first] = checker.get(first)
			print(f"{first} is head")
		if  (pointed_checker.get(sec) == None):
			pointed_checker[sec] = checker.get(sec)
			print(f"{sec} was point")

	for k,v in head_checker.items():
		if (pointed_checker.get(k) == None):
			ret_list.append(v)
			print(f"append {k} to heads")
	
	return (ret_list)

def	get_intersec(nodes, heads):
	passed = []
	intersec = []
	for head in heads:
		curr = head
		while (curr):
			if (curr not in passed):
				passed.append(curr)
			elif (curr not in intersec):
				intersec.append(curr)
				break
			curr = curr.next
	return (intersec)

def	remove_intersec(nodes, heads, intersec):
	new_heads = []
	need_head = 0
	for head in heads:
		curr = head
		while (curr):
			if (need_head):
				new_heads.append(curr)
				need_head = 0
			tmp = curr.next
			if (curr.next in intersec):
				print(f"{curr.next.value} is in intersec")
				tmp = tmp.next
				curr.next = None
				need_head = 1
			curr = tmp
	return (new_heads)
	




ll = LinkedList()
nodes = dict()
inp = input("Enter edges: ").split(',')
for i in inp:
	ele = i.split('>')
	first = int(ele[0])
	sec = int(ele[1])
	# print(checker.get(first))
	if (nodes.get(first) == None):
		nodes.update({first: Node(first)})
	if (nodes.get(sec) == None):
		nodes.update({sec: Node(sec)})

join_node(inp, nodes)
print(nodes)
heads = get_heads(inp, nodes)
# get intersection
intersec = get_intersec(nodes, heads)
print(intersec)
# remove intersec
print(f"new head is {remove_intersec(nodes, heads, intersec)}")
for head in heads:
	curr = head
	while (curr):
		print(curr.value, end="->")
		curr = curr.next
	print()
	print('---')
# get new head
# swap merge

