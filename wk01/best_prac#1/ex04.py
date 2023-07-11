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
cnt = 0
u1 = t1[:]
u2 = t2[:]
while (True):
    cnt += 1
    u1 = rotate(u1)
    u2 = reverse_rotate(u2)
    if (cnt < 6 or (u1 == t1 and u2 == t2)):
        print(f"{cnt} {u1} {u2}")
    elif (cnt == 6):
        print(" . . . . . ")
    if (u1 == t1 and u2 == t2):
        break
        
print(f"Total of  {cnt} rounds.")

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
