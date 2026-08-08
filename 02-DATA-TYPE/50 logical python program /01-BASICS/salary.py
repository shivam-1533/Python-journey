# Calculate the net salary of an employee.

# Take the basic salary as input.
basic_salary = float(input("Enter your basic salary: "))

# Calculate allowances.
hra = basic_salary * 0.20
da = basic_salary * 0.10

# Calculate the gross salary.
gross_salary = basic_salary + hra + da

# Calculate the deduction.
pf = basic_salary * 0.12

# Calculate the net salary.
net_salary = gross_salary - pf

# Display the salary details.
print("\n========== SALARY DETAILS ==========")
print(f"Basic Salary : ₹{basic_salary:.2f}")
print(f"HRA          : ₹{hra:.2f}")
print(f"DA           : ₹{da:.2f}")
print(f"Gross Salary : ₹{gross_salary:.2f}")
print(f"PF Deduction : ₹{pf:.2f}")
print(f"Net Salary   : ₹{net_salary:.2f}")
print("====================================")
