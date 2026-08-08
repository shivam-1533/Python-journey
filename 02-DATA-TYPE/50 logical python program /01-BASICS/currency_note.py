# Calculate the total currency amount based on the number of notes.

# Take the user's name as input.
name = input("Enter your name: ")

# Take the count of each denomination as input.
count_2000 = int(input("Enter the number of ₹2000 notes: "))
count_1000 = int(input("Enter the number of ₹1000 notes: "))
count_500 = int(input("Enter the number of ₹500 notes: "))
count_200 = int(input("Enter the number of ₹200 notes: "))
count_100 = int(input("Enter the number of ₹100 notes: "))
count_50 = int(input("Enter the number of ₹50 notes: "))
count_20 = int(input("Enter the number of ₹20 notes: "))
count_10 = int(input("Enter the number of ₹10 notes: "))

# Calculate the total amount from all denominations.
amount = (
    (count_2000 * 2000)
    + (count_1000 * 1000)
    + (count_500 * 500)
    + (count_200 * 200)
    + (count_100 * 100)
    + (count_50 * 50)
    + (count_20 * 20)
    + (count_10 * 10)
)

# Display the total amount.
print(f"\nYour total amount is: ₹{amount}")
print(f"Thank you, {name}! 🙏")
