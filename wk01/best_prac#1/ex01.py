# จงคำนวณค่า BMI โดยมีสูตรการคำนวณดังนี้

# BMI = น้ำหนักหน่วย (kg) / ( ความสูงหน่วย (m) * ความสูงหน่วย (m))

# โดยมีเกณฑ์ดังต่อไปนี้

# ค่า                             สถานะ

# BMI < 18.5               Below normal weight

# 18.5 <= BMI < 25     Normal weight

# 25 <= BMI < 30        Overweight

# 30 <= BMI < 35        Case I Obesity

# 35 <= BMI < 40        Case II Obesity

# BMI >= 40                Case III Obesity

#  *** BMI ***
# Enter your weight(kg) and height(m) : 48 1.68
# Your status is : Below normal weight.

print(" *** BMI *** ")
w,h = map(float, input("Enter your weight(kg) and height(m) : ").split())
bmi = w / (h * h)
print("Your status is : ", end = "")
if (bmi < 18.5):
	print("Below normal weight.")
elif (bmi < 25):
	print("Normal weight.")
elif (bmi < 30):
	print("Overweight.")
elif (bmi < 35):
	print("Case I Obesity.")
elif (bmi < 40):
	print("Case II Obesity.")
else :
	print("Case III Obesity.")


