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

	def	set_node(self, src, dst):
		i,curr = 0, self.head
		dst_node = None
		src_node = None
		if (self.isEmpty()):
			print("Error! {list is empty}")
		
		while (curr):
			if (i == src):
				src_node = curr
			if (i == dst):
				dst_node = curr
			curr = curr.next
			i += 1
		if  (src_node and dst_node):
			src_node.next = dst_node
		else:
			
	
	def	is_loop(self):
		cnt = 0
		first = self.head
		curr = self.head
		while (curr):
			if (cnt != 0 and curr is first):
				return (True)
			else:
				cnt += 1
			curr = curr.next
		return (False)


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
	mode,param = i.split()
	if mode == "A":
		L.append(param)
	elif mode == "S":
		src,dst = param.split(':')
		L.set_node(int(src), int(dst))
		if (L.is_loop()):
			print("Found Loop")
		else:
			print("No Loop")
	
	print(L)
