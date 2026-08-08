# Calculate the electricity bill based on the number of units consumed.

# Take the electricity consumption as input.
units = int(input("Enter the number of units consumed: "))

# Calculate the bill based on the applicable rate.
if units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = units * 2.5

elif units <= 300:
    bill = units * 4

else:
    bill = units * 6

# Display the calculated electricity bill.
print(f"Electricity Bill = ₹{bill:.2f}")
