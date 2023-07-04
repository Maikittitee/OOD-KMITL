print(" *** Rank score ***")
ip = input("Enter ID and Score end with ID : ").split()
n_list = []
s_list = []
for i in range(len(ip)):
    if (i % 2 == 0 and ip[i] in n_list):
        ending = ip[i]
        break
    if (i % 2 == 0):
        n_list.append(ip[i])
    else:
        s_list.append(float(ip[i]))

my_dict = dict(zip(n_list, s_list))
sorted_dict = dict(sorted(my_dict.items(), key=lambda x:x[1]))

print(my_dict)
print(ending)
print(sorted_dict)
print(ending[0])