class Queue:
	def __init__(self):
		self.queue = []
	def is_empty(self):
		if len(self.queue) <= 0:
			return 1
		return 0
	def enqueue(self, obj):
		self.queue.append(obj)
		
	def dequeue(self):
		return self.queue.pop(0)

	def front(self):
		if len(self.queue) == 0:
			return None
		return self.queue[0]
	def __len__(self):
		return len(self.queue)
	def __repr__(self):
		return str(self.queue)

command = list(map(str, input("Enter Input : ").split(',')))
row = Queue()
xrow = Queue()
for ele in command:
	mode = str(ele[:2])
	if mode == "EN":
		id = int(ele[3:])
		row.enqueue(id)
	if mode == "ES":
		id = int(ele[3:])
		xrow.enqueue(id)
	if mode == 'D':
		if xrow.is_empty():
			if row.is_empty():
				print("Empty")
			else:
				print(row.dequeue())
		else:
			print(xrow.dequeue())
			