
# ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

# การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

# ***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

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