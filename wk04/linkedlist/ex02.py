class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None
		

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def __str__(self):
		curr, s = self.head, ""
		while curr != None:
			if (curr.next != None):
				s += str(curr.data) + "->"
			else:
				s += str(curr.data) + " "
			curr = curr.next
		return s
	
	def str_reverse(self):
		curr, s = self.tail, ""
		while curr != None:
			if (curr.previous != None):
				s += str(curr.data) + "->"
			else:
				s += str(curr.data) + " "
			curr = curr.previous
		return s	


	def isEmpty(self):
		return self.head == None

	def append(self, item):
		new_node = Node(item)
		if (self.isEmpty()):
			self.tail = new_node
			self.head = new_node
		else:
			curr = self.head
			while (curr.next):
				curr = curr.next
			curr.next = new_node
			new_node.previous = curr
			self.tail = new_node
		
	def	add_front(self, item):
		new_node = Node(item)
		if (self.isEmpty()):
			self.tail = new_node
			self.head = new_node
		else:
			tmp = self.head
			self.head = new_node
			new_node.next = tmp
			tmp.previous = new_node

	def insert(self, index:int, data):
		curr, i = self.head, 0
		new_node = Node(data)
		if (index == 0):
			print(f"index = {index} and data = {data}")
			self.add_front(data)
			return
		else:
			while (curr):
				if (i == index - 1):
					print(f"index = {index} and data = {data}")
					if (curr.next != None):
						new_node.previous = curr
						new_node.next = curr.next
						curr.next = new_node
						new_node.next.previous = new_node
					else:
						self.append(data)
					return
				curr = curr.next
				i += 1
			print("Data cannot be added")


	def remove(self, data):
		curr, i = self.head, 0
		while (curr):
			if (curr.data == data):
				print(f"removed : {data} from index : {i}")
				if (i == 0):
					self.head = curr.next
					if (self.isEmpty()):
						self.tail = None
					if (curr.next):
						curr.next.previous = None
					if (self.head):
						self.head.previous = None
				elif (curr.next == None):
					curr.previous.next = None
					self.tail = curr.previous
				else:
					curr.previous.next = curr.next
					curr.next.previous = curr.previous
				return 
			curr = curr.next
			i += 1
		print("Not Found!")
	

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
	mode,param = i.split()
	if mode == "A":
		L.append(param)
	elif mode == "Ab":
		L.add_front(param)	
	elif mode == "I":
		param = param.split(':')
		L.insert(int(param[0]), param[1])
	elif mode == "R":
		L.remove(param)
	print(f"linked list : {L}")
	print(f"reverse : {L.str_reverse()}")

