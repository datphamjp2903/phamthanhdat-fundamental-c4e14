h = int(input("Your height(cm):"))
w = int(input("Your weight(kg):"))
hcm = h/100
BMI = w / (hcm*hcm)
print(BMI)
if BMI < 16:
    print("Severely underweight")
elif BMI >= 16 and BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")
