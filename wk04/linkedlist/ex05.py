class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)
	

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

def createLL(LL):
	new = LinkedList()
	for i in LL:
		new.append(i)
	return (new)

		

def printLL(head:LinkedList):
	curr = head.head
	while (curr != None):
		print(curr.value, end = " ")
		curr = curr.next
	print()

def SIZE(head):
	curr = head.head
	i = 0
	while (curr != None):
		i += 1
		curr = curr.next
	return (i)

def	do_buttom_up(head:LinkedList, b, size):
	new_list = LinkedList()
	n_up = int(size * b/100)
	curr = head.head
	for i in range(n_up - 1):
		curr = curr.next
	buttom_head = curr.next
	curr.next = None
	curr = buttom_head
	while (curr.next):
		curr = curr.next
	curr.next = head.head
	head.head = buttom_head
	
def	do_riffle(head:LinkedList, r, size):
	new_list = LinkedList()
	n_up = int(size * r/100)
	curr = head.head
	for i in range(n_up - 1):
		curr = curr.next
	buttom_head = curr.next
		


def scarmble(head:LinkedList, b, r, size):
	# buttom up
	print(f"Start : ", end = '')
	printLL(head)
	print(f"BottomUp {float(size)} % : ", end = '')
	do_buttom_up(b, size)
	printLL(head)
	print(f"Riffle {float(size)} % : ", end='')
	do_riffle(head, r, size)



	# Code Here
	pass

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
printLL(h.head)
print()
do_buttom_up(h, 50, SIZE(h))
printLL(h.head)
# for i in inp2.split('|'):
	# print("Start : {0}".format(printLL(h)))
	# k = i.split(',')
	# if k[0][0] == "B" and k[1][0] == "R":
	# 	scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
	# elif k[0][0] == "R" and k[1][0] == "B":
	# 	scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
	# print('-' * 50)