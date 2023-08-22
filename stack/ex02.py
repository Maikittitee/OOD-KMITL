
stack = []
couple = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "]" : None,
    ")" : None,
    "}" : None
    
}
err = 0
opening = ["(", "[", "{"]
# จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

# โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

# 1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

# 2. วงเล็บปิดเกิน

# 3. วงเล็บเปิดเกิน

# แล้วให้แสดงผลตามตัวอย่าง

closing = [")", "]", "}"]

s = str(input("Enter expresion : "))

def	match(open, close):
    if (couple[open] == close):
        return (True)
    return (False)

print(s, end=" ")
for c in s:
    # print(stack)
    if c in opening:
        stack.append(c)
    else:
        if c in closing:
            if (len(stack) > 0):
                if not match(stack.pop(), c):
                    print("Unmatch open-close ")
                    err = 1
                    break
            else:
                print("close paren excess")
                err = 1
                break
                

def stack_str(s: list):
    return ("".join(i for i in s))

if (err == 0 and len(stack) > 0):
    print(f"open paren excess   {len(stack)} : {stack_str(stack)}")
elif (err == 0):
    print("MATCH")
		

