# Calculate the electricity bill based on the units consumed

customer_name = input("Enter your name: ").strip()
account_id = input("\nEnter your account ID: ")

# Validate the customer's name.
if not customer_name.isalpha():
    print("Your name is not valid.")
    exit()

print("\n<===== Login Successful =====>\n")

# Take the total units consumed by the customer.
units = float(input("Enter units consumed: "))

# Calculate the bill according to the unit range.
if units <= 100:
    net_bill = units * 5

elif units <= 200:
    net_bill = units * 7

else:
    net_bill = units * 10

print(f"\nYour Net Bill is: ₹{net_bill:.2f}\n")
