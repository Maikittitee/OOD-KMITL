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

def	check_map(width: int, height: int, map_d):
	cnt = 0
	for i in map_d:
		if (len(i) != width):
			return (False)
		cnt += 1
	if (cnt != height):
		return (False)
	return (True)

def	find_start_xy(height, width, map_d):
	for y in range(height):
		for x in range(width):
			if (map_d[y][x] == 'F'):
				return x,y
	return -1,-1

def	is_valid(maze, new):
	x = new[0]
	y = new[1]
	if (0 <= x < len(maze[0]) and 0 <= y < len(maze)):
		return (True)
	return (False)

q = Queue()
size = input("Enter width, height, and room: ").split()
maze = size[2].split(",")

if (not check_map(int(size[0]), int(size[1]), maze)):
	print("Invalid map input.")


x_start, y_start = find_start_xy(int(size[1]), int(size[0]), maze)

x = x_start
y = y_start

q.enqueue(tuple([x_start, y_start]))
print(f"Queue: {q}")
while (True):
	something = list(q.peek())
	x = something[0]
	y = something[1]
	print(f"xyyyy{x},{y}")
	if (maze[y][x] == 'O'):
		print("Found the exit portal.")
		break
	tmp = q.dequeue()
	tmp = list(tmp)
	for i in range(4):
		new = tmp
		if (i == 0):
			new[1] -= 1
		if (i == 1):
			new[0] += 1
		if (i == 2):
			new[1] += 1
		if (i == 3):
			new[0] -= 1
	if (is_valid(maze, new)):
		q.enqueue(tuple(new))
	
	# print(f"Queue: {q}")
		
