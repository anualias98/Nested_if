#calculate the BMI
height=float(input("Enter your height in m:"))
weight=float(input("Enter your weight in kg:"))
bmi=(weight/height **2)
if bmi<18.5:
    print("Your bmi is",bmi,"you are underweight")
elif bmi<25:
    print("Your bmi is", bmi, "you are normal weight")
elif bmi<30:
    print("Your bmi is", bmi, "you are slightly overweight")
elif bmi<35:
    print("Your bmi is", bmi, "you are obese")
else:
    print("Your bmi is", bmi, "you are clinically obese")
