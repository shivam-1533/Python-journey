# Calculate the rental cost based on car type and rental duration.

# Display available cars.
print("========== CAR RENTAL ==========")
print("1. Sedan  - ₹1500/day")
print("2. SUV    - ₹2500/day")
print("3. Luxury - ₹5000/day")
print("4. Sports - ₹8000/day")

# Take car selection and rental days as input.
choice = int(input("Enter your car choice: "))
days = int(input("Enter number of rental days: "))

# Validate the number of days.
if days <= 0:
    print("Invalid number of days.")

else:
    # Determine the daily rental price.
    if choice == 1:
        car_name = "Sedan"
        daily_rate = 1500

    elif choice == 2:
        car_name = "SUV"
        daily_rate = 2500

    elif choice == 3:
        car_name = "Luxury"
        daily_rate = 5000

    elif choice == 4:
        car_name = "Sports"
        daily_rate = 8000

    else:
        car_name = ""
        daily_rate = 0
        print("Invalid car choice.")

    # Continue only if a valid car was selected.
    if daily_rate > 0:
        total = daily_rate * days

        # Apply a long-term discount.
        if days >= 15:
            discount_percentage = 20

        elif days >= 7:
            discount_percentage = 10

        else:
            discount_percentage = 0

        discount = total * discount_percentage / 100

        # Add a weekend surcharge.
        if days >= 2:
            surcharge = total * 0.05

        else:
            surcharge = 0

        final_amount = total - discount + surcharge

        # Display the rental bill.
        print("\n========== RENTAL BILL ==========")
        print(f"Car Type        : {car_name}")
        print(f"Rental Days     : {days}")
        print(f"Base Amount     : ₹{total:.2f}")
        print(f"Discount        : ₹{discount:.2f}")
        print(f"Weekend Charge  : ₹{surcharge:.2f}")
        print(f"Final Amount    : ₹{final_amount:.2f}")
        print("=================================")
