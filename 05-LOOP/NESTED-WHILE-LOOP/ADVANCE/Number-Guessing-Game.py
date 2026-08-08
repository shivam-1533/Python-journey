# Create a multi-round number guessing game using nested while loops.

print("======================================")
print("        NUMBER GUESSING GAME")
print("======================================")

player_name = input("Enter your name: ")
score = 0
round_number = 1

# Start multiple game rounds.
while True:
    print(f"\n========== ROUND {round_number} ==========")
    print("Choose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty = int(input("Enter difficulty: "))

    if difficulty == 1:
        secret = 5
        max_attempts = 5

    elif difficulty == 2:
        secret = 27
        max_attempts = 4

    elif difficulty == 3:
        secret = 73
        max_attempts = 3

    else:
        print("Invalid difficulty.")
        continue

    attempts = 1
    won = False

    # Allow multiple guesses in one round.
    while attempts <= max_attempts:
        guess = int(input(f"\nAttempt {attempts}/{max_attempts}: "))

        if guess == secret:
            print("\n🎉 Correct! You won this round.")
            score += (max_attempts - attempts + 1) * 10
            won = True
            break

        elif guess < secret:
            print("Too low. Try a higher number.")

        else:
            print("Too high. Try a lower number.")

        attempts += 1

    if not won:
        print(f"\nYou lost this round. The number was {secret}.")

    print(f"Current Score: {score}")

    again = input("\nPlay another round? (yes/no): ").lower()

    if again != "yes":
        break

    round_number += 1

print("\n======================================")
print("             GAME OVER")
print("======================================")
print(f"Player : {player_name}")
print(f"Score  : {score}")
print("======================================")
