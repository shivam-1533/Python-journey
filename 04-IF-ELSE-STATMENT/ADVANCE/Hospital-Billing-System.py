# Calculate a hospital bill based on treatment and room charges.

# Take patient details as input.
patient_name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

# Display room options.
print("\n========== ROOM TYPES ==========")
print("1. General Room - ₹1000/day")
print("2. Private Room - ₹3000/day")
print("3. ICU          - ₹8000/day")

room_choice = int(input("Enter room choice: "))
days = int(input("Enter number of days: "))

# Determine the room charge.
if room_choice == 1:
    room_name = "General Room"
    room_rate = 1000

elif room_choice == 2:
    room_name = "Private Room"
    room_rate = 3000

elif room_choice == 3:
    room_name = "ICU"
    room_rate = 8000

else:
    room_name = "Invalid"
    room_rate = 0

# Continue if the room choice is valid.
if room_rate == 0:
    print("Invalid room choice.")

else:
    # Take treatment costs as input.
    doctor_fee = float(input("Enter doctor consultation fee: ₹"))
    medicine_cost = float(input("Enter medicine cost: ₹"))
    test_cost = float(input("Enter test cost: ₹"))

    emergency = input("Was it an emergency? (yes/no): ").lower()
    insurance = input("Do you have insurance? (yes/no): ").lower()

    # Calculate room charges.
    room_cost = room_rate * days

    # Add emergency charges if applicable.
    if emergency == "yes":
        emergency_charge = 2000

    else:
        emergency_charge = 0

    # Calculate the total bill.
    total_bill = room_cost + doctor_fee + medicine_cost + test_cost + emergency_charge

    # Apply insurance discount.
    if insurance == "yes":
        insurance_discount = total_bill * 0.20

    else:
        insurance_discount = 0

    final_bill = total_bill - insurance_discount

    # Display the hospital bill.
    print("\n========== HOSPITAL BILL ==========")
    print(f"Patient Name       : {patient_name}")
    print(f"Age                : {age}")
    print(f"Room Type          : {room_name}")
    print(f"Room Charges       : ₹{room_cost:.2f}")
    print(f"Doctor Fee         : ₹{doctor_fee:.2f}")
    print(f"Medicine Cost      : ₹{medicine_cost:.2f}")
    print(f"Test Cost          : ₹{test_cost:.2f}")
    print(f"Emergency Charges  : ₹{emergency_charge:.2f}")
    print(f"Insurance Discount : ₹{insurance_discount:.2f}")
    print(f"Final Bill         : ₹{final_bill:.2f}")
    print("===================================")
