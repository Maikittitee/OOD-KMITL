
opening = {
    '(' : ')',
    '[': ']',
    ')':None,
    ']':None
}
couple = {
    '(' : ')',
    '[': ']',
    ')': '(',
    ']': '['
}
stack = []
close_stack = []
# close = [")","]"]
def	is_couple(s1, s2):
    if (couple[s1] == s2):
        return (True)
    return (False)
    
             
def	count_no_couple(s):
    for i in range(len(s)):
        c = s[i]
        if (opening[c] != None):
            stack.append(c)
        elif is_couple(c, stack[len(stack)- 1]):
            stack.pop()
        else:
             close_stack.append(c)
    return (len(stack) + len(close_stack))
        

# print(opening[')'])
#;
ret = count_no_couple(str(input("Enter Input : ")))
print(ret)
if (ret == 0):
	print("Perfect ! ! !")

# stack.append("a");
# stack.append("b")
# print(stack)