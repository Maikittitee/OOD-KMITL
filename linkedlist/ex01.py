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

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
	if i[:2] == "AP":
		L.append(i[3:])
	elif i[:2] == "AH":
		L.addHead(i[3:])
	elif i[:2] == "SE":
		print("{0} in {1}".format(L.search(i[3:]), L))
	elif i[:2] == "SI":
		print("Linked List size = {0} : {1}".format(L.size(), L))
	elif i[:2] == "ID":
		print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
	elif i[:2] == "PO":
		before = "{}".format(L)
		k = L.pop(int(i[3:]))
		print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
