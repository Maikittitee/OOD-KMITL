lst = list(map(int, input("Enter All Bid : ").split(' ')))
if (len(lst) <= 1):
	print("not enough bidder")
else:
	lst.sort(reverse=True)
	max = lst[0]
	if (max == lst[1]):
		print("error : have more than one highest bid")
	else:
		sec = lst[1]
		print(f"winner bid is {max} need to pay {sec}")
