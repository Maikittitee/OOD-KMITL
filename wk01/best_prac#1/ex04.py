def rotate(str1):
 
    # Create the extended string and index of for rotation
    temp = str1 + str1
    l1 = len(str1)
    l2 = len(temp)
    str= temp[l1-1 : l2-1]
    return (str)
 
def reverse_rotate(str1):
    temp = str1 + str1
    l1 = len(str1)
    l2 = len(temp)
    str = temp[1  : l1+1]
    return (str)
     
 
print("*** String Rotation ***")
t1,t2 = input("Enter 2 strings : ").split()
c = 1
# u1 = t1[:]
# u2 = t2[:]
t = 1
u1 = rotate(t1)
u2 = reverse_rotate(t2)
print(f"{c} {u1} {u2}")
while (u1 != t1 or u2 != t2):
	c += 1
	u1 = rotate(u1)
	u2 =reverse_rotate(u2)
	if (c <= 6 and t == 1):
		print(f"{c} {u1} {u2}")
	elif (t == 1):
		t = 0
		print(" . . . . . ")
	if (c > 5 and u1 == t1 and u2 == t2):
		print(f"{c} {u1} {u2}")


print(f"Total of  {c} rounds.")

# *** String Rotation ***
# Enter 2 strings : debate string
# 1 edebat trings
# 2 tedeba ringst
# 3 atedeb ingstr
# 4 batede ngstri
# 5 ebated gstrin
# 6 debate string
# Total of  6 rounds.

# *** String Rotation ***
# Enter 2 strings : Marvel Stinger
# 1 lMarve tingerS
# 2 elMarv ingerSt
# 3 velMar ngerSti
# 4 rvelMa gerStin
# 5 arvelM erSting
#  . . . . . 
# 42 Marvel Stinger
# Total of  42 rounds.
