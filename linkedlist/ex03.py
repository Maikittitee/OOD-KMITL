
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
		cur, s = self.head, ""
		while cur != None:
			if (cur.next == None):
				s += str(cur.value) + ""
			else:
				s += str(cur.value) + " -> "
			cur = cur.next
		return s

	def isEmpty(self):
		return self.head == None

	def append(self, new_node):
		if (self.isEmpty()):
			self.head = new_node
			tmp = new_node.next
			new_node.next = None
			return (tmp)
		else:
			curr = self.head
			while (curr.next):
				curr = curr.next
			curr.next = new_node
			tmp = new_node.next
			new_node.next = None
			return (tmp)

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
		first = ele[0]
		sec = ele[1]
		checker.get(first).next = checker.get(sec)

def	get_heads(inp, checker):
	head_checker = dict()
	pointed_checker = dict()
	ret_list = []
	for i in inp:
		ele = i.split('>')
		first = ele[0]
		sec = ele[1]
		if (head_checker.get(first) == None):
			head_checker[first] = checker.get(first)
		if  (pointed_checker.get(sec) == None):
			pointed_checker[sec] = checker.get(sec)
	for k,v in head_checker.items():
		if (pointed_checker.get(k) == None):
			ret_list.append(v)
	return (ret_list)

def	get_intersec(nodes, heads):
	passed = []
	intersec = []
	for head in heads:
		curr = head
		while (curr):
			if (curr not in passed):
				passed.append(curr)
			else:
				intersec.append(curr)
				break
			curr = curr.next
	return (set(intersec))

def	remove_intersec(nodes, heads, intersec):
	for head in heads:
		curr = head
		while (curr):
			tmp = curr.next
			if (tmp in intersec):
				curr.next = None
				tmp = tmp.next
				if (tmp not in heads):
					heads.append(tmp)
			curr = tmp

def	sorting_head(heads,  nodes):
	sorted_heads = []
	key = list(map(int, nodes.keys()))
	key.sort()
	sorted_nodes = {str(i) : nodes[str(i)] for i in key}
	for addr in sorted_nodes.values():
		if (addr in heads):
			sorted_heads.append(addr)
	return (sorted_heads)

def ft_size_promax(node, intersec):
		passed = []
		curr,cnt = node,0
		while (curr):
			passed.append(curr)
			curr = curr.next
			cnt += 1
			if (curr in passed):
				break
		return (cnt)

def ft_size(node):
		curr,cnt = node,0
		while (curr):
			curr = curr.next
			cnt += 1
		return (cnt)

def	max_size(heads):
	max = 0
	for head in heads:
		if (ft_size(head) > max):
			max = ft_size(head)
	return (max)
		

def	swap_merge(heads):
	ll = LinkedList()
	lim = max_size(heads)
	currs = [head for head in heads]
	i = 0
	j = 0
	while (i < lim):
		j = 0
		for curr in currs:
			if (curr != None):
				tmp = curr
				currs[j] = ll.append(tmp)
			j += 1
		i += 1
	return (ll)

def	print_intersec(intersec):
	for node in intersec:
		print(f"Node({node.value}, size={ft_size_promax(node, intersec)})")

def	remove_intersec_head(heads:list, intersec):
	tmps = [i for i in heads]
	for tmp in tmps:
		if (tmp in intersec):
			heads.remove(tmp)

nodes = dict()
inp = input("Enter edges: ").split(',')
for i in inp:
	ele = i.split('>')
	first = ele[0]
	sec = ele[1]
	if (nodes.get(first) == None):
		nodes.update({first: Node(first)})
	if (nodes.get(sec) == None):
		nodes.update({sec: Node(sec)})

join_node(inp, nodes)
# print(nodes)
heads = get_heads(inp, nodes)
# get intersection
intersec = get_intersec(nodes, heads)
intersec = sorting_head(intersec, nodes)
if (len(intersec) == 0):
	print("No intersection")
	exit()
# print(intersec)
else:
	print_intersec(intersec)
# remove intersec
# get new head
remove_intersec(nodes, heads, intersec)
remove_intersec_head(heads, intersec)
# sorting head
heads = sorting_head(heads, nodes)
# print(heads)
# for head in heads:
# 	curr = head
# 	while (curr):
# 		print(curr.value, end="->")
# 		curr = curr.next
# 	print()
# 	print('---')
# ok i can get it
# swap merge
print("Delete intersection then swap merge:")
ll = swap_merge(heads)
print(ll)


