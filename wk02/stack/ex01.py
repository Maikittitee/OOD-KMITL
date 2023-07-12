 
# ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่  โดยให้แสดงผลลัพธ์ออกมาเป็นจำนวนวงเล็บที่จะต้องเติมหากวงเล็บมีไม่ครบคู่   แต่ถ้าหากครบคู่ให้แสดงคำว่า  Perfect  ออกมาด้วย

opening = {
    '(' : ')',
    '[' : ']',
    ')' : None,
    ']' : None
}

closing = {
    '(' : None,
    '[' : None,
    ')' : '(',
    ']' : '['
}


couple = {
    '(' : ')',
    '[' : ']',
    ')' : '(',
    ']' : '['
}
open_stack = []
close_stack = []


def	is_couple(s1, s2):
    if (couple[s1] == s2):
        return (True)
    return (False)
    
             
def	count_no_couple(s):
    for i in range(len(s)):
        c = s[i]
        if (opening[c] != None):
            open_stack.append(c)
        elif (closing[c] != None):
            if (len(open_stack) > 0 and is_couple(c, open_stack[-1])):
                open_stack.pop()
            else:
                close_stack.append(c)
        else:
             close_stack.append(c)
    return (len(open_stack) + len(close_stack))
        

# print(opening[')'])
#;
ret = count_no_couple(str(input("Enter Input : ")))
print(ret)
if (ret == 0):
	print("Perfect ! ! !")

# stack.append("a");
# stack.append("b")
# print(stack)