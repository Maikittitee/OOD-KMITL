


def get_unique_partition(l:list, n:int, sum, target) -> list:
	checker = l[0]
	if (n == 0):
		return ('0')
	if (n == 1):
		return ('1')
	l.append(get_unique_partition(l, n - 1))
		
	return ()



l = []
n, s = list(map(int, input("Enter n, s: ").split()))
l.append([n])
print(get_unique_partition(l, n))

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
