# Calculate the number of currency notes required for a given amount.

# Take the user's first and last name as input.
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Validate that both names contain letters only.
if not (first_name.isalpha() and last_name.isalpha()):
    print(
        "\n[ERROR] Invalid input! Names must contain letters only "
        "(no numbers or symbols). Program stopped."
    )
    exit()

# Take the total amount as input.
amount = int(input("Enter the total amount: "))

# Calculate the number of ₹500 notes.
note_500 = amount // 500
amount %= 500

# Calculate the number of ₹100 notes.
note_100 = amount // 100
amount %= 100

# Calculate the number of ₹50 notes.
note_50 = amount // 50
amount %= 50

# Calculate the number of ₹20 notes.
note_20 = amount // 20
amount %= 20

# Calculate the number of ₹10 notes.
note_10 = amount // 10
amount %= 10

# Display the currency note breakdown.
print("\n--- Currency Notes Breakdown ---")
print("₹500 Notes :", note_500)
print("₹100 Notes :", note_100)
print("₹50 Notes  :", note_50)
print("₹20 Notes  :", note_20)
print("₹10 Notes  :", note_10)

# Display any remaining amount below ₹10.
if amount > 0:
    print("Remaining Balance :", amount)

# Display a thank-you message.
print(f"\nThank you, {first_name} {last_name}! 🙏")
