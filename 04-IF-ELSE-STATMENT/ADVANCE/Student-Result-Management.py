# Calculate a student's total marks, percentage, and grade.

# Take the student's name and marks as input.
name = input("Enter student name: ")

maths = float(input("Enter marks in Mathematics: "))
english = float(input("Enter marks in English: "))
science = float(input("Enter marks in Science: "))
computer = float(input("Enter marks in Computer: "))
hindi = float(input("Enter marks in Hindi: "))

# Calculate total marks and percentage.
total = maths + english + science + computer + hindi
percentage = total / 5

# Check whether the student passed all subjects.
if maths >= 40 and english >= 40 and science >= 40 and computer >= 40 and hindi >= 40:
    result = "Pass"

    # Determine the grade based on percentage.
    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    else:
        grade = "D"

else:
    result = "Fail"
    grade = "F"

# Display the result.
print("\n========== STUDENT RESULT ==========")
print(f"Student Name : {name}")
print(f"Total Marks  : {total:.2f}/500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
print(f"Result       : {result}")
print("====================================")
