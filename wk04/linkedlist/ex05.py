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
	s = ""
	while (curr != None):
		s += str(curr.value) + " "
		curr = curr.next
	return (s)

def SIZE(head):
	curr = head.head
	i = 0
	while (curr != None):
		i += 1
		curr = curr.next
	return (i)

def	do_buttom_up(head:LinkedList, b, size):
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
	n_up = int(size * r/100)
	curr = head.head
	for i in range(n_up):
		tmp3 = curr
		curr = curr.next
	target_head = curr
	old_head = head.head
	tmp1 = old_head.next
	tmp2 = target_head.next
	while (tmp2 != None and old_head.value != tmp3.value):
		old_head.next = target_head
		old_head = tmp1
		tmp1 = old_head.next
		target_head.next = old_head
		target_head = tmp2
		tmp2 = target_head.next
		if (tmp2 != None):
			old_head.next = target_head
	if (tmp2 == None and old_head.value != tmp3.value):
		target_head.next = old_head.next
		curr = old_head.next
		while (curr.next.value != tmp3.next.value):
			curr=curr.next
		curr.next = None
		old_head.next = target_head
	elif (old_head.value == tmp3.value and tmp2 != None):
		old_head.next = target_head
	else:
		old_head.next = target_head

def	do_deriffle(head:LinkedList, r:float, size:int):
	do_riffle(head, r, size)
	do_riffle(head, r, size)
	do_riffle(head, r, size)
	do_riffle(head, r, size)
	do_riffle(head, r, size)
	do_riffle(head, r, size)
	do_riffle(head, r, size)
	do_riffle(head, r, size)

	# size - 1
	



def	dup_ll(head):
	new_list = LinkedList()
	curr = head.head
	while (curr != None):
		new_list.append(curr.value)
		curr = curr.next
	return (new_list)
def scarmble(head:LinkedList, b:float, r:float, size):
	start_linklist = dup_ll(head, )
	print(f"BottomUp {b:.3f} % : ", end = '')
	do_buttom_up(head, b, size)
	print(printLL(head))
	buttom_upped_linklist = dup_ll(head)
	print(f"Riffle {r:.3f} % : ", end='')
	do_riffle(head, r, size)
	print(printLL(head))
	print(f"Deriffle {r:.3f} % : ", end='')
	# do_deriffle(head, r, size)
	head.head = buttom_upped_linklist.head
	print(printLL(head))
	print(f"Debottomup {b:.3f} % : ", end = '')
	head.head = start_linklist.head
	print(printLL(head))

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
# do_deriffle(h, 30, SIZE(h))
for i in inp2.split('|'):
	print("Start : {0}".format(printLL(h)))
	k = i.split(',')
	if k[0][0] == "B" and k[1][0] == "R":
		scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
	elif k[0][0] == "R" and k[1][0] == "B":
		scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
	print('-' * 50)