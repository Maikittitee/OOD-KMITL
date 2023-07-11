color_stack = []

def	bomb():
    count = 0
    if (len(color_stack) == 0):
        return (False)
    index = len(color_stack) - 1
    target = color_stack[index]
    while (index >= 0):
        if (color_stack[index] == target):
            count += 1
        if (count >= 3):
            return (True)
        index -= 1
    return (False)
        
    
    
    


s = input("Enter Input : ").split()
count = 0
for i in s:
	if (not bomb()):
		color_stack.append(i)
	if (bomb()):
		count += 1
		color_stack.pop()
		color_stack.pop()
		color_stack.pop()

n = "".join(i for i in color_stack)
print(len(n))
if (len(n) != 0):
	print(n[::-1])
else:
	print("Empty")
if (count > 1):
	print(f"Combo : {count} ! ! !")

# color_stack = ["B",'A', 'A', "A", "A"]
# print(bomb())
# color_stack.pop()
# color_stack.pop()
# color_stack.pop()
# print(bomb())
# print(color_stack)