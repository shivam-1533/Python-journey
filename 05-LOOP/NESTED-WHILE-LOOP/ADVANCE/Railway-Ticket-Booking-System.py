# Create a railway ticket booking system using nested while loops.

print("======================================")
print("       RAILWAY BOOKING SYSTEM")
print("======================================")

available_seats = 20
total_bookings = 0
total_revenue = 0

# Main railway menu.
while True:
    print("\n========== RAILWAY MENU ==========")
    print("1. Book Ticket")
    print("2. Check Available Seats")
    print("3. Train Information")
    print("4. Cancel Booking")
    print("5. Exit")
    print("==================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if available_seats <= 0:
            print("No seats available.")
            continue

        print("\n========== TRAINS ==========")
        print("1. Delhi Express")
        print("2. Mumbai Express")
        print("3. Kolkata Express")

        train_choice = int(input("Select train: "))

        if train_choice == 1:
            train_name = "Delhi Express"
            base_fare = 800

        elif train_choice == 2:
            train_name = "Mumbai Express"
            base_fare = 1200

        elif train_choice == 3:
            train_name = "Kolkata Express"
            base_fare = 1000

        else:
            print("Invalid train.")
            continue

        passengers = int(input("Enter number of passengers: "))

        if passengers <= 0:
            print("Invalid passenger count.")
            continue

        if passengers > available_seats:
            print("Not enough seats available.")
            continue

        passenger_number = 1
        booking_total = 0

        # Process every passenger.
        while passenger_number <= passengers:
            print(f"\n========== PASSENGER {passenger_number} ==========")

            name = input("Enter passenger name: ")
            age = int(input("Enter passenger age: "))

            # Calculate fare according to age.
            if age < 5:
                fare = 0
                category = "Child"

            elif age >= 60:
                fare = base_fare * 0.60
                category = "Senior Citizen"

            elif age < 18:
                fare = base_fare * 0.75
                category = "Child/Teen"

            else:
                fare = base_fare
                category = "Adult"

            booking_total += fare

            print(f"Passenger : {name}")
            print(f"Category  : {category}")
            print(f"Fare      : ₹{fare:.2f}")

            passenger_number += 1

        available_seats -= passengers
        total_bookings += passengers
        total_revenue += booking_total

        print("\n======================================")
        print("            TICKET BOOKED")
        print("======================================")
        print(f"Train             : {train_name}")
        print(f"Passengers        : {passengers}")
        print(f"Total Fare        : ₹{booking_total:.2f}")
        print(f"Available Seats   : {available_seats}")
        print("======================================")

    elif choice == 2:
        print(f"\nAvailable Seats: {available_seats}")

    elif choice == 3:
        print("\n========== TRAIN INFORMATION ==========")
        print("Delhi Express   : Delhi to Jaipur")
        print("Mumbai Express  : Delhi to Mumbai")
        print("Kolkata Express : Delhi to Kolkata")
        print("=======================================")

    elif choice == 4:
        if total_bookings == 0:
            print("No booking available for cancellation.")
            continue

        cancel = int(input("Enter number of tickets to cancel: "))

        if cancel <= 0:
            print("Invalid number.")

        elif cancel > total_bookings:
            print("You cannot cancel more tickets than booked.")

        else:
            available_seats += cancel
            total_bookings -= cancel

            print(f"{cancel} ticket(s) cancelled successfully.")

    elif choice == 5:
        print("\n======================================")
        print("        RAILWAY SYSTEM CLOSED")
        print("======================================")
        print(f"Total Tickets Booked : {total_bookings}")
        print(f"Total Revenue        : ₹{total_revenue:.2f}")
        print("Thank you for using our service.")
        break

    else:
        print("Invalid choice.")
