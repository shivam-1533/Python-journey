# Check whether a customer is eligible for a loan.

# Take customer information as input.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: ₹"))
credit_score = int(input("Enter your credit score: "))
existing_loan = input("Do you have an existing loan? (yes/no): ").lower()
employment = input("Are you employed? (yes/no): ").lower()

# Check basic eligibility conditions.
if age < 18:
    print("Not eligible. You must be at least 18 years old.")

elif salary < 20000:
    print("Not eligible. Minimum monthly salary is ₹20,000.")

elif employment != "yes":
    print("Not eligible. Employment is required.")

else:
    # Determine the credit score category.
    if credit_score >= 750:
        credit_category = "Excellent"

    elif credit_score >= 650:
        credit_category = "Good"

    else:
        credit_category = "Low"

    # Determine the final loan status.
    if credit_score >= 750 and existing_loan == "no":
        status = "Eligible"

    elif credit_score >= 650:
        status = "Needs Manual Verification"

    else:
        status = "Not Eligible"

    # Display the result.
    print("\n========== LOAN ELIGIBILITY ==========")
    print(f"Applicant Name   : {name}")
    print(f"Credit Category  : {credit_category}")
    print(f"Loan Status      : {status}")
    print("======================================")
