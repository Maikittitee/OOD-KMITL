'''รับจำนวนเต็มมา 1 จำนวนแล้วให้แสดงผลดังนี้

- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Metadrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากน้อยไปมาก และมีตัวซ้ำให้แสดงผลว่า "Plaindrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และไม่มีตัวซ้ำเลยให้แสดงผลว่า "Katadrome"

- หาก input ที่รับมานั้นมีการเรียงลำดับจากมากไปน้อย และมีตัวซ้ำให้แสดงผลว่า "Nialpdrome"

- หาก input ที่รับมานั้นทุกหลักเป็นเลขเดียวกันหมด ให้แสดงผลว่า "Repdrome"

- หากไม่อยู่ในเงื่อนไขด้านบนเลย ให้แสดงผลว่า "Nondrome"

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง'''

def foo(s):
	prev = 0
	prev2 = 10
	passed = []
	assending = True
	decending = True
	cnt = 0
	dup = False
	all_same = False
	for i in s:
		n = int(i)
		if (n in passed):
			dup = True
			cnt += 1
		if (prev > n):
			assending = False
		if (prev2 < n):
			decending = False
		passed.append(int(i))
		prev = n
		prev2 = n
	if (cnt + 1 == len(s)):
		all_same = True

	# print(f"assen: {assending}, decen: {decending}, dup: {dup}, allsame: {all_same}")
	if (assending and not dup):
		return ("Metadrome")
	if (assending and dup and not all_same):
		return ("Plaindrome")
	if (decending and not dup):
		return ("Katadrome")
	if (decending and dup and not all_same):
		return ("Nialpdrome")
	if (all_same):
		return ("Repdrome")
	return ("Nondrome")

		

inp = input("Enter Input : ")


print(foo(inp))
