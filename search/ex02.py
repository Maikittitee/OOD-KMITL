inp = input("Enter Input : ").split('/')
nums = list(map(int, inp[0].split()))
targets = list(map(int, inp[1].split()))

for target in targets:
	min = None
	for i in range(1, 1000):
		if (target + i in nums):
			min = target + i
			break
	if (min):
		print(min)
	else:
		print("No First Greater Value")

