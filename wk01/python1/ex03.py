print("*** Reading E-Book ***")
text, target = input("Text , Highlight : ").split(',')
for i in text:
    if (i == target):
        print(f"[{target}]", end = "")
    else:
        print(i, end = "")
print()
                