# Calculate the hotel booking bill.

# Take customer details as input.
customer_name = input("Enter customer name: ")

# Display room options.
print("\n========== ROOM OPTIONS ==========")
print("1. Single Room - ₹2000/day")
print("2. Double Room - ₹3500/day")
print("3. Deluxe Room - ₹5000/day")
print("4. Suite       - ₹8000/day")

# Take room selection and number of days.
room_choice = int(input("Enter room choice: "))
days = int(input("Enter number of days: "))

# Determine the room price.
if room_choice == 1:
    room_name = "Single Room"
    room_rate = 2000

elif room_choice == 2:
    room_name = "Double Room"
    room_rate = 3500

elif room_choice == 3:
    room_name = "Deluxe Room"
    room_rate = 5000

elif room_choice == 4:
    room_name = "Suite"
    room_rate = 8000

else:
    room_name = ""
    room_rate = 0

# Check whether the room selection is valid.
if room_rate == 0:
    print("Invalid room choice.")

else:
    # Take additional service costs.
    food_cost = float(input("Enter food charges: ₹"))
    room_service = float(input("Enter room service charges: ₹"))
    extra_bed = input("Do you need an extra bed? (yes/no): ").lower()

    # Calculate extra bed charges.
    if extra_bed == "yes":
        extra_bed_charge = 1000 * days

    else:
        extra_bed_charge = 0

    # Calculate room charges.
    room_cost = room_rate * days

    # Apply a long-stay discount.
    if days >= 7:
        discount_percentage = 15

    elif days >= 3:
        discount_percentage = 5

    else:
        discount_percentage = 0

    # Calculate the subtotal.
    subtotal = room_cost + food_cost + room_service + extra_bed_charge

    discount = subtotal * discount_percentage / 100
    final_amount = subtotal - discount

    # Display the hotel bill.
    print("\n========== HOTEL BILL ==========")
    print(f"Customer Name     : {customer_name}")
    print(f"Room Type         : {room_name}")
    print(f"Number of Days    : {days}")
    print(f"Room Charges      : ₹{room_cost:.2f}")
    print(f"Food Charges      : ₹{food_cost:.2f}")
    print(f"Room Service      : ₹{room_service:.2f}")
    print(f"Extra Bed         : ₹{extra_bed_charge:.2f}")
    print(f"Discount          : ₹{discount:.2f}")
    print(f"Final Amount      : ₹{final_amount:.2f}")
    print("================================")
