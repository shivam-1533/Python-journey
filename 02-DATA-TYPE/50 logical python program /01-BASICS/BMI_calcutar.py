# Calculate BMI and determine the corresponding weight category.

# Take weight in kilograms and height in feet as input.
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (feet): "))

# Convert height from feet to meters.
height_in_meters = height * 0.3048

# Calculate BMI.
bmi = weight / (height_in_meters**2)

# Determine the BMI category.
if bmi <= 18.5:
    print(f"\nYour BMI is {bmi:.2f} - Underweight.")

elif bmi <= 24.9:
    print(f"\nYour BMI is {bmi:.2f} - Normal weight.")

elif bmi <= 29.9:
    print(f"\nYour BMI is {bmi:.2f} - Overweight.")

else:
    print(f"\nYour BMI is {bmi:.2f} - Obese.")

# Display a health reminder.
print("\nPlease take care of yourself!")
