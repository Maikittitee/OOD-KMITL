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
s = input("Enter Input : ").split(",")
for i in s:
	if i[0] == 'E':
		print(f"Add {i[2:]} index is {len(q)}")
		q.enqueue(i[2:])
	elif i[0] == 'D':
		if len(q) != 0:
			print(f"Pop {q.peek()} size in queue is {len(q)-1}")
			q.dequeue()
		else:
			print("-1")
if (len(q) == 0):
	print("Empty")
else:
	print(f"Number in Queue is :  {q}")
