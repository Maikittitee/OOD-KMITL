

def	is_colli(a:int, b:int):
	if (a < 0 and b > 0):
		return (True)
	return (False)
	  

def asteroid_collision(curr: int, asts:list) -> list:
	# base case
	if ( len(asts) <= 1):
		return ([asts[0]])
	if (is_colli(curr, asts[0])):
		if (abs(curr) > abs(asts[0])):
			win = [curr]
		elif (abs(curr) < abs(asts[0])):
			win = [asts[0]]
		else:
			win = []
	else:
		win = [curr, asts[0]]
	return (win + asteroid_collision(asts[0], asts[1:])) 

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x[0], x[1:]))