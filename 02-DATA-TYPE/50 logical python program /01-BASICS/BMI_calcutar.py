#  WRITE A PROGRAM TO FIND BMI FOR A GOOD WEALTH

weight = float(input("Enter your 'Weight': "))

height = float(input("\nEnter your 'Height': "))

bmi = weight / ((height * 0.3048) ** 2)

if bmi <= 18.5:
    print("\nYour BMI Is in Underweight",bmi,"\n")

elif bmi <= 24.9:
    print("\nYour BMI is Normal Healthy weight",bmi,"\n")

elif bmi <= 29.9:
    print("\nYour BMI is Overweight",bmi,"\n")

else:
    print("\nYour BMI is 'Obese'",bmi,"\n")

print("--Please Take Care Of Yourself-- \n")