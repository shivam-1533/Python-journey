# Simulate a simple mobile recharge system.

# Take the mobile number as input.
mobile_number = input("Enter your mobile number: ")

# Display available recharge plans.
print("\n========== RECHARGE PLANS ==========")
print("1. ₹199 - 1.5 GB/day")
print("2. ₹299 - 2 GB/day")
print("3. ₹399 - 2.5 GB/day")
print("4. ₹599 - 3 GB/day")

# Take the plan choice as input.
choice = int(input("Enter your plan choice: "))

# Determine the selected plan.
if choice == 1:
    amount = 199
    data = "1.5 GB/day"
    validity = "28 Days"

elif choice == 2:
    amount = 299
    data = "2 GB/day"
    validity = "28 Days"

elif choice == 3:
    amount = 399
    data = "2.5 GB/day"
    validity = "56 Days"

elif choice == 4:
    amount = 599
    data = "3 GB/day"
    validity = "84 Days"

else:
    amount = 0
    data = ""
    validity = ""

# Display the recharge details.
if amount > 0:
    print("\n========== RECHARGE SUCCESSFUL ==========")
    print(f"Mobile Number : {mobile_number}")
    print(f"Plan Amount   : ₹{amount}")
    print(f"Data          : {data}")
    print(f"Validity      : {validity}")
    print("Recharge completed successfully.")
    print("=========================================")

else:
    print("Invalid plan choice.")
