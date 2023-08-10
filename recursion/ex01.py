def	get_min_recur(l):
    if (len(l) == 1):
        return (l[0])
    return (min(l[0], get_min_recur(l[1:])))

inp = list(map(int, input("Enter Input : ").split()))
print(f"Min : {get_min_recur(inp)}")