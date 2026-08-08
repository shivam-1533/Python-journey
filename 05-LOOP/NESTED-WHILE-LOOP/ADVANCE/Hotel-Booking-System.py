# Create a hotel booking and billing system using nested while loops.

print("======================================")
print("          HOTEL BOOKING SYSTEM")
print("======================================")

total_bookings = 0

# Keep the booking system active.
while True:
    print("\n========== HOTEL MENU ==========")
    print("1. Book Room")
    print("2. Check Room Prices")
    print("3. Hotel Information")
    print("4. Exit")
    print("================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_name = input("\nEnter customer name: ")
        age = int(input("Enter customer age: "))

        print("\n========== ROOM TYPES ==========")
        print("1. Single Room  - ₹2000/day")
        print("2. Double Room  - ₹3500/day")
        print("3. Deluxe Room  - ₹5000/day")
        print("4. Suite        - ₹8000/day")

        room_choice = int(input("Select room: "))

        if room_choice == 1:
            room_name = "Single Room"
            room_price = 2000

        elif room_choice == 2:
            room_name = "Double Room"
            room_price = 3500

        elif room_choice == 3:
            room_name = "Deluxe Room"
            room_price = 5000

        elif room_choice == 4:
            room_name = "Suite"
            room_price = 8000

        else:
            print("Invalid room choice.")
            continue

        days = int(input("Enter number of nights: "))

        if days <= 0:
            print("Invalid number of nights.")
            continue

        room_total = room_price * days

        food = 0
        service = 0

        # Add additional services.
        while True:
            print("\n========== SERVICES ==========")
            print("1. Add Food")
            print("2. Room Service")
            print("3. Extra Bed")
            print("4. Finish Services")

            service_choice = int(input("Choose service: "))

            if service_choice == 1:
                food = float(input("Enter food charges: ₹"))

            elif service_choice == 2:
                service = float(input("Enter room service charges: ₹"))

            elif service_choice == 3:
                extra_bed = 1000 * days
                print(f"Extra bed charges: ₹{extra_bed}")

            elif service_choice == 4:
                break

            else:
                print("Invalid service.")

        if "extra_bed" not in locals():
            extra_bed = 0

        subtotal = room_total + food + service + extra_bed

        # Apply long-stay discount.
        if days >= 15:
            discount_rate = 20

        elif days >= 7:
            discount_rate = 15

        elif days >= 3:
            discount_rate = 5

        else:
            discount_rate = 0

        discount = subtotal * discount_rate / 100
        final_amount = subtotal - discount

        print("\n======================================")
        print("             HOTEL BILL")
        print("======================================")
        print(f"Customer       : {customer_name}")
        print(f"Age            : {age}")
        print(f"Room           : {room_name}")
        print(f"Nights         : {days}")
        print(f"Room Charges   : ₹{room_total:.2f}")
        print(f"Food Charges   : ₹{food:.2f}")
        print(f"Room Service   : ₹{service:.2f}")
        print(f"Extra Bed      : ₹{extra_bed:.2f}")
        print(f"Discount       : ₹{discount:.2f}")
        print("--------------------------------------")
        print(f"Final Amount   : ₹{final_amount:.2f}")
        print("======================================")

        total_bookings += 1

    elif choice == 2:
        print("\n========== ROOM PRICES ==========")
        print("Single Room : ₹2000/day")
        print("Double Room : ₹3500/day")
        print("Deluxe Room : ₹5000/day")
        print("Suite       : ₹8000/day")

    elif choice == 3:
        print("\n========== HOTEL INFORMATION ==========")
        print("Check-in  : 12:00 PM")
        print("Check-out : 11:00 AM")
        print("Free Wi-Fi available.")
        print("24/7 room service available.")

    elif choice == 4:
        print(f"\nTotal bookings today: {total_bookings}")
        print("Thank you for using our hotel system.")
        break

    else:
        print("Invalid choice.")
