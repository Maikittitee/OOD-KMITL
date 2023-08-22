def	print_list_space(lst):
    for i in lst:
        print(i, end="  ")
    print()

print(" *** String count ***")
text = input("Enter message : ")
up = []
low = []
up = [i for i in text if i.isupper()]
low = [i for i in text if i.islower()]

up_final = [*set(up)]
low_final = [*set(low)]

print(f"No. of Upper case characters : {len(up)}")
print("Unique Upper case characters : ", end = "")
print_list_space(sorted(up_final))
print(f"No. of Lower case Characters : {len(low)}")
print("Unique Lower case characters : ", end = "")
print_list_space(sorted(low_final))

#  *** String count ***
# Enter message : I Love KMITL.
# No. of Upper case characters : 7
# Unique Upper case characters : I  K  L  M  T  
# No. of Lower case Characters : 3
# Unique Lower case characters : e  o  v  