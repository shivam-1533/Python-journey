# Calculate the compound interest on a loan.

# Take the principal amount, interest rate, time, and compounding frequency as input.
principal = float(input("Enter the principal amount of your loan: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the loan duration (years): "))
frequency = float(input("Enter the number of times interest is compounded per year: "))

# Calculate the final amount using the compound interest formula.
amount = principal * (1 + (rate / 100) / frequency) ** (frequency * time)

# Calculate the compound interest earned.
compound_interest = amount - principal

# Display the compound interest and final amount.
print(f"Compound interest: {compound_interest:.2f}")
print(f"Total amount: {amount:.2f}")
