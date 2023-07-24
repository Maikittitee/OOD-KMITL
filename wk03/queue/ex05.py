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

def is_that_path_possible(start_x, start_y, map_d, paths:str):
	i = start_y
	j = start_x
	for path in paths:
		if (path == 'L'):
			j -= 1
		if (path == 'R'):
			j += 1
		if (path == 'D'):
			i += 1
		if (path == 'U'):
			i -= 1
	
	if not (0 <= j < len(map_d[0]) and 0 <= i < len(map_d)):
		print(f"{j},{i} is out")
		return (False)
	elif (map_d[i][j] == '#'):
		return (False)
	return (True)



def	is_that_path_can_find_portal(start_x, start_y, map_d, paths:str):
	i = start_y
	j = start_x
	for path in paths:
		if (path == 'L'):
			j -= 1
		if (path == 'R'):
			j += 1
		if (path == 'D'):
			i += 1
		if (path == 'U'):
			i -= 1
	if (map_d[i][j] == 'O'):
		print("FOUNDDDDDD")
		print(paths)
		return (True)
	return (False)

if __name__ == "__main__":
	size = input("Enter width, height, and room: ").split()
	map_d = size[2].split(",")
	
	if (not check_map(int(size[0]), int(size[1]), map_d)):
		print("Invalid map input.")
	else:
		print("doing")
	q = Queue()
	add = ""
	q.enqueue("")
	cnt = 0
	start_x, start_y = find_start_xy(int(size[1]), int(size[0]), map_d)
	if (start_x == -1 or start_y == -1):
		print("No starting Point ?")
	print(f"starting point is {start_x},{start_y}")
	while not is_that_path_can_find_portal(start_x, start_y, map_d, add):
		add = q.dequeue()
		for j in ["L", "R", "U", "D"]:
			put = add + j
			if (is_that_path_possible(start_x, start_y, map_d, put)):
				q.enqueue(put)
		cnt += 1
		# if (cnt == 4):
		# 	break
	print(q)
		# print("ok")
	# display solution