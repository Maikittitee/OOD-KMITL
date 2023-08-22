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

def is_that_point_possible(map_d, pnt):
	pnt = list(pnt)
	if not (0 <= pnt[0] < len(map_d[0]) and 0 <= pnt[1] < len(map_d)):
		return (False)
	elif (map_d[pnt[1]][pnt[0]] != '_' and map_d[pnt[1]][pnt[0]] != 'O' and map_d[pnt[1]][pnt[0]] != 'F'):
		return (False)
	return (True)

def	fill(s, i):
	new = []
	for cnt in range(len(s)):
		if cnt == i:
			new.append("#")
		else:
			new.append(s[cnt])
	return("".join(new))	


def	display_point(map_d, start_x, start_y, paths):
	new = []
	new.append(tuple([start_x, start_y]))
	print(f"Queue: {new}")
	for path in paths:
		temp = list(new.pop(0))
		map_d[temp[1]] = fill(map_d[temp[1]], temp[0])
		if (0 <= temp[0] < len(map_d[0]) and 0 <= temp[1] - 1 < len(map_d) and map_d[temp[1] - 1][temp[0]] == '_'):
			new.append(tuple([temp[0], temp[1] - 1]))
		if (0 <= temp[0] + 1 < len(map_d[0]) and 0 <= temp[1] < len(map_d) and map_d[temp[1]][temp[0] + 1] == '_'):
			new.append(tuple([temp[0] + 1, temp[1]]))
		if (0 <= temp[0] < len(map_d[0]) and 0 <= temp[1] + 1 < len(map_d) and map_d[temp[1] + 1][temp[0]] == '_'):
			new.append(tuple([temp[0], temp[1] + 1]))
		if (0 <= temp[0] - 1< len(map_d[0]) and 0 <= temp[1] < len(map_d) and map_d[temp[1]][temp[0]- 1] == '_'):
			new.append(tuple([temp[0] - 1, temp[1]]))
		if (path == 'U'):
			temp[1] -= 1
		if (path == 'R'):
			temp[0] += 1
		if (path == 'D'):
			temp[1] += 1
		if (path == 'L'):
			temp[0] -= 1
		if (0 <= temp[0] < len(map_d[0]) and 0 <= temp[1] < len(map_d)):
		# 	# new.append(tuple(temp))
			if (map_d[temp[1]][temp[0]] != 'O'):
				print(f"Queue: {new}")
	print("Found the exit portal.")
		
		
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
		# print("FOUNDDDDDD")
		# print(paths)
		# display_point(map_d, start_x, start_y, paths)
		return (True)
	return (False)

def	gogo(old_pnt, j):
	new_point = list(old_pnt)
	if (j == 'U'):
		new_point[1] -= 1
	if (j == 'R'):
		new_point[0] += 1
	if (j == 'D'):
		new_point[1] += 1
	if (j == 'L'):
		new_point[0] -= 1
	return (tuple(new_point))


if __name__ == "__main__":
	size = input("Enter width, height, and room: ").split()
	map_d = size[2].split(",")
	
	if (not check_map(int(size[0]), int(size[1]), map_d)):
		print("Invalid map input.")
	q = Queue()
	add = ""
	# q.enqueue("")
	cnt = 0
	start_x, start_y = find_start_xy(int(size[1]), int(size[0]), map_d)
	if (start_x == -1 or start_y == -1):
		print("No starting Point ?")
	q.enqueue(tuple([start_x, start_y]))
	while not is_that_path_can_find_portal(start_x, start_y, map_d, add):
		if len(q) == 0:
			print('Cannot reach the exit portal.')
			break
		old = q.dequeue()
		for j in ["U", "R", "D", "L"]:
			put = gogo(old, j)
			if (is_that_point_possible(map_d, put)):
				q.enqueue(put)
			tmp = list(put)
			x = tmp[0]
			y = tmp[1]
			if (map_d[y][x] == "O"):
				print("Found the exit portal.")
				
		print(f"Queue: {q}")
		cnt += 1