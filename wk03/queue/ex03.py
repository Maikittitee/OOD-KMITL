class Queue:
	def __init__(self, list=[]):
		self.items = list

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		if self.items:
			return self.items.pop(0)

	def peek(self):
		if self.items:
			return self.items[0]

	def __len__(self):
		return len(self.items)

	def __str__(self):
		return str(self.items)

	def __repr__(self):
		return str(self)

q = Queue()
s = input("input : ").split(",")
n_cnt = 0
in_err = 0
de_err = 0	

def	do_de(s, de_err):
	n = int(s)
	lenq = len(q)
	err = n - lenq
	for i in range(lenq):
		q.dequeue()
	return (err)

def	input_error(s):
	if (s[0] == 'D'):
		return (False)
	if (s[0] == 'E'):
		return (False)
	return (True)

def	do_en(s, n_cnt):
	n = int(s)
	for i in range(n):
		q.enqueue("*"+str(i + n_cnt))
	return (n)

def	print_step(s):
	print(f"Step : {s}")
	if (s[0] == 'E'):
		print("Enqueue : ", end = "")
	if (s[0] == 'D'):
		print("Dequeue : ", end = "")
	print(q)
	print(f"Error Dequeue : {de_err}")
	print(f"Error input : {in_err}")
	print("--------------------")

for i in s:
	if (input_error(i)):
		in_err += 1
	elif i[0] == 'D':
		de_err += do_de(i[1:], de_err)
	elif i[0] == 'E':
		n_cnt += do_en(i[1:], n_cnt)
	print_step(i)

