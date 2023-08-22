print("*** multiplication or sum ***")
n1,n2 = map(int, input("Enter num1 num2 : ").split(' '))
multi = n1 * n2
if (multi > 1000):
	print(f"The result is {n1 + n2}")
else:
	print(f"The result is {multi}")
	

