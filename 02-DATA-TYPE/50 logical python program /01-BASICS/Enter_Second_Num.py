# Calculate simple interest.

# Take the principal amount, rate of interest, and time as input.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time: "))

# Calculate the simple interest.
simple_interest = (principal * rate * time) / 100

# Display the calculated simple interest.
print(f"Your simple interest is: ₹{simple_interest:.2f}")
