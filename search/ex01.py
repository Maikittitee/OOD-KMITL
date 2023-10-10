inp = list(input("input : ").split(','))
c, r = list(map(int, inp[0].split()))
ele = list(map(int, inp[1].split()))
# print(c)
# print(r)
# print(ele)

maze = []
# add to maze

a = 0
for i in range(r):
	curr = []
	for j in range(c):
		curr.append(ele[a])
		a += 1
	maze.append(curr)

# print(maze)

# get small less row

min = 99999999
target_row = -1
for i in range(len(maze)):
	for j in range(len(maze[i])):
		if (maze[i][j] < min):
			min = maze[i][j]
			target_row = i

# get max column of that row

max = -1
target_column = -1
for i in range(len(maze[target_row])):
	if (maze[target_row][i] > max):
		max = maze[target_row][i]
		target_column = i

max = -1

for row in maze:
	if (row[target_column] > max):
		max = row[target_column]

print(max)

		



