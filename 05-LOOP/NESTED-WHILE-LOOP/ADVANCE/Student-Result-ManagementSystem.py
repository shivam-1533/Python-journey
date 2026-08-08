# Create a student result management system using nested while loops.

print("======================================")
print("      STUDENT RESULT SYSTEM")
print("======================================")

student_number = 1
class_total = 0
class_students = 0

# Process multiple students.
while True:
    print(f"\n========== STUDENT {student_number} ==========")

    name = input("Enter student name: ")

    print("\nEnter marks for five subjects.")

    subject = 1
    total = 0
    failed_subjects = 0

    # Enter marks for all five subjects.
    while subject <= 5:
        if subject == 1:
            subject_name = "Mathematics"

        elif subject == 2:
            subject_name = "English"

        elif subject == 3:
            subject_name = "Science"

        elif subject == 4:
            subject_name = "Computer"

        else:
            subject_name = "Hindi"

        marks = float(input(f"Enter marks in {subject_name}: "))

        if marks < 0 or marks > 100:
            print("Invalid marks. Enter marks between 0 and 100.")
            continue

        total += marks

        if marks < 40:
            failed_subjects += 1

        subject += 1

    percentage = total / 5

    # Determine grade.
    if failed_subjects > 0:
        grade = "F"
        result = "Fail"

    elif percentage >= 90:
        grade = "A+"
        result = "Pass"

    elif percentage >= 80:
        grade = "A"
        result = "Pass"

    elif percentage >= 70:
        grade = "B"
        result = "Pass"

    elif percentage >= 60:
        grade = "C"
        result = "Pass"

    else:
        grade = "D"
        result = "Pass"

    # Display the student's result.
    print("\n======================================")
    print("           STUDENT RESULT")
    print("======================================")
    print(f"Student Name : {name}")
    print(f"Total Marks  : {total}/500")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")
    print(f"Failed       : {failed_subjects} Subject(s)")
    print("======================================")

    class_total += percentage
    class_students += 1

    more = input("\nAdd another student? (yes/no): ").lower()

    if more != "yes":
        break

    student_number += 1


# Display class statistics.
if class_students > 0:
    class_average = class_total / class_students

    print("\n======================================")
    print("          CLASS SUMMARY")
    print("======================================")
    print(f"Total Students : {class_students}")
    print(f"Class Average  : {class_average:.2f}%")
    print("======================================")
