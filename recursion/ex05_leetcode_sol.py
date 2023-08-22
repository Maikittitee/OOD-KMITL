def fn(i, st):
	if not st:
		st.append(i)
		return
	else:
		if st[-1]<0:
			st.append(i)
			return
		else:
			if i>0:
				st.append(i)
				return
			else:
				if abs(i) == st[-1]:
					st.pop()
					return
				else:
					x = st.pop()
					if abs(i)>abs(x):
						fn(i, st)
					else:
						fn(x, st)
					return
				
def ft_map_promax_ultra(st, aster):
	if (len(aster) <= 0):
		return
	fn(aster[0], st)
	ft_map_promax_ultra(st, aster[1:])
	
def asteroid_collision(aster: list) -> list:
	st = []
		# for i in aster:
		#     fn(i, st)
	ft_map_promax_ultra(st, aster)
	return st

x = input("Enter Input : ")
if (' ' in x):
	x = x.split(", ")
else:
	x = x.split(",")
x = list(map(int,x))
print(asteroid_collision(x))