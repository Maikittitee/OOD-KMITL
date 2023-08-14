

n, s = list(map(int, input("Enter n, s: ").split()))

def get_par(n: int, nofone: int) -> str:
	if (n == 0):
		return ('0')
	if (n == 1):
		return ('1')
	print(n, end = '+')
	print()
	return (get_par(n - 1, nofone + 1) + '+' + get_par(n - 2, 0))


print(get_par(n, 0))
	