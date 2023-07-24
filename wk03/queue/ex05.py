class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		return self.queue.pop(0)

	def is_empty(self):
		return len(self.queue) == 0

	def size(self):
		return len(self.queue)
	
	def in_front(self):
		return self.queue[0]

def	check_map(width: int, height: int, map_d):
	cnt = 0
	for i in map_d:
		if (len(i) != width):
			return (False)
		cnt += 1
	if (cnt != height):
		return (False)
	return (True)


if __name__ == "__main__":
	size = input("Enter width, height, and room: ").split()
	map_d = size[2].split(",")
	
	if (not check_map(int(size[0]), int(size[1]), map_d)):
		print("Invalid map input.")
	else:
		print("doing")