print(" *** Rank score ***")
ip = input("Enter ID and Score end with ID : ").split()
n_list = []
s_list = []
for i in range(len(ip)):
    if (i % 2 == 0):
        n_list.append(ip[i])
    else:
        s_list.append(float(ip[i]))
target = ip[i]
my_dict = dict(zip(n_list, s_list))
# sorted_dict = dict(sorted(my_dict.items(), key=lambda x:x[1]))

print(ip[0:-1])
print(target)
print(my_dict)

cnt = 0
for i in my_dict.keys():
    cnt += 1
    if (i == target):
        print(cnt)