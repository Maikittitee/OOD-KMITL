def integer_partition(n, target, result, ans):
    if n == 0:
        ans.append(' + '.join(map(str, result)))
        return
    i = min(target, n)
    if i > 0:
        result.append(i)
        integer_partition(n - i, i, result, ans)
        result.pop()
        integer_partition(n, i - 1, result, ans)

def	display_ans(ans, lim, i, point):
	if (lim == i or len(ans) == i):
		if (point == 1):
			print(". . .")
		return
	print(ans[i])
	display_ans(ans, lim, i + 1, point)
	

ans = []
res = []
n, s = list(map(int, input("Enter n, s: ").split()))
# l.append([n])
if (n == 0):
	ans.append("0")
else:
	integer_partition(n, n, res, ans)

# print(ans)
# print(res)
if (len(ans) > s):
	display_ans(ans, s, 0, 1)
else:
	display_ans(ans, s, 0, 0)
print(f"Total: {len(ans)}")

# def partition_helper(n, max_val, current_partition):
#     if n == 0:
#         print(current_partition)
#         return
	
#     for i in range(1, min(n, max_val) + 1):
#         partition_helper(n - i, i, current_partition + [i])

# def generate_partitions(n):
#     partition_helper(n, n, [])

# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     print(f"All number partitions of {n} are:")
#     generate_partitions(n)
