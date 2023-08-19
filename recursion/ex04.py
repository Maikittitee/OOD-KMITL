

def get_unique_partition(n, max, l) -> list:
	if (n == 0):
		print(f"when max is {max} is work!")
		return (1)
	if (n < 0 or max == 0):
		return (0)
	return (get_unique_partition(n - max, max, l) + get_unique_partition(n, max - 1, l))



l = []
n, s = list(map(int, input("Enter n, s: ").split()))
# l.append([n])
print(f"there have {get_unique_partition(n, n, l)} solutions");

print()
print(l)

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
