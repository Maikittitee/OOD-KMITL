
def asteroid_collision(curr, aster: list, st = []) -> list:
	if (len(aster) == 0):
		return
	if not st:
		st.append(curr)
	else:
		if (st[-1] < 0):
			st.append(curr)
			return
		else:
			if (curr > 0):
				st.append(curr)
			else:
				if (abs(curr) == abs(st[-1])):
					st.pop()
				else:
					x = st.pop()
					if (abs(curr) > abs(x)):
						asteroid_collision(curr, aster, st)
					else:
						asteroid_collision(x, aster, st)

def ft_map_promax_ultra(st, aster):
	if (len(aster) <= 0):
		return
	asteroid_collision(aster[0], aster, st)
	ft_map_promax_ultra(st, aster[1:])	

def trim_space_recur(curr, inp: list):
	if (len(inp) <= 0):
		return
	curr 

st = []
x = input("Enter Input : ")
# if (' ' in x):
# 	x = x.split(", ")
# else:
x = x.split(",")
x = list(map(int, map(lambda x: x.strip(), x)))
ft_map_promax_ultra(st, x)
# asteroid_collision(x[0], x, st)
print(st)