def	isPrime(n):
		if n <= 1:
			return False
		if n <= 3:
			return True
		if n % 2 == 0 or n % 3 == 0:
			return False

		i = 5
		while i * i <= n:
			if n % i == 0 or n % (i + 2) == 0:
				return False
		i += 6
		return True

class MyInt:
	def	__init__(self, n):
		self.n = n

	def isPrime(self):
		if self.n < 2:
			return False
		for i in range(2, self.n):
			if self.n% i == 0:
				return False
		return True

	
	def __str__(self):
		return str(self.n)

	def	showPrime(self):

		run = MyInt(2)
		s = " ".join(str(n) for n in range(self.n + 1) if isPrime(n))
		if s == "":
			return ("!!!A prime number is a natural number greater than 1")
		return (s)

	def	__sub__(self, other):
		return (self.n - other.n // 2)
	
	
# a = MyInt(23)

# b = MyInt(17)

# print(a.isPrime())

# print(b.isPrime())

# print(a.showPrime())

# print(b.showPrime())

# print(a-b)

print(" *** class MyInt *** ")
n1, n2 = map(int, input("Enter 2 number : ").split())
n1 = MyInt(n1)
n2 = MyInt(n2)
print(f"{n1} isPrime : {n1.isPrime()}")
print(f"{n2} isPrime : {n2.isPrime()}")
print(f"Prime number between 2 and {n1} : {n1.showPrime()}")
print(f"Prime number between 2 and {n2} : {n2.showPrime()}")
print(f"{n1} - {n2} = {n1 - n2}")