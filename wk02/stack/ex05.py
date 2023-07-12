print("******** Parking Lot ********")

ip = input("Enter max of car,car in soi,operation : ").split()
# print(ip)
#ip[0] = Number of lot
#ip[1] = list of car
#ip[2] = mode 
#ip[3] = target

nlot = int(ip[0])
if (ip[1] == '0'):
    stack = []
else:
	stack = ip[1].split(",")
mode = ip[2]
target = ip[3]

if (mode == "arrive"):
    if (target in stack):
        print(f"car {target} already in soi")
    elif (len(stack) == nlot):
        print(f"car {target} cannot arrive : Soi Full")
    else:
        stack.append(target)
        print(f"car {target} arrive! : Add Car {target}")

elif (mode == "depart"):
    if (len(stack) == 0):
        print(f"car {target} cannot depart : Soi Empty")
    elif (target not in stack):
        print(f"car {target} cannot depart : Dont Have Car {target}")
    else:
        stack.remove(target)
        print(f"car {target} depart ! : Car {target} was remove")

stack = list(map(int, stack))
# if (len(stack) == 0):
#     print("[]")
# else:
print(stack)