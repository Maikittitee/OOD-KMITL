def	look_back(stack):
	cnt = 1
	if (len(stack) == 0):
		return (0)
	stack.reverse()
	max = stack[0]
	for i in stack:
		if (i > max):
			max = i
			cnt += 1
	return (cnt)


s = input("Enter Input : ").split(',')
stack = []
for i in s:
	new = i.split()
	if (new[0] == 'A'):
		stack.append(int(new[1]))
	if (new[0] == 'B'):
		print(look_back(stack))
		stack.reverse()

# print(stack)               
# stack.reverse()
# print(stack)               
        
