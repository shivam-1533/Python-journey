# Determine the age category: Child, Teenager, Adult, or Senior Citizen.

# Take the user's age as input.
age = int(input("Enter your age: "))

# Determine the age category based on the given age.
if age < 8:
    print("You are a child.")

elif age <= 21:
    print("You are a teenager.")

elif age <= 60:
    print("You are an adult.")

else:
    print("You are a senior citizen.")
