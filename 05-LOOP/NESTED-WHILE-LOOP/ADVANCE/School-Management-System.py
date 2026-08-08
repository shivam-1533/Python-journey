# Create a school management system using nested while loops.

print("==========================================")
print("         SCHOOL MANAGEMENT SYSTEM")
print("==========================================")

# Basic system counters.
student_count = 0
teacher_count = 0
total_fees = 0

# Main school management menu.
while True:
    print("\n==========================================")
    print("              SCHOOL MENU")
    print("==========================================")
    print("1. Student Management")
    print("2. Teacher Management")
    print("3. Attendance")
    print("4. Marks and Result")
    print("5. Fee Management")
    print("6. School Report")
    print("7. Exit")
    print("==========================================")

    choice = int(input("Enter your choice: "))

    # Student management.
    if choice == 1:

        while True:
            print("\n========== STUDENT MANAGEMENT ==========")
            print("1. Add Student")
            print("2. View Student Information")
            print("3. Search Student")
            print("4. Back")
            print("========================================")

            student_choice = int(input("Enter your choice: "))

            if student_choice == 1:
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                class_name = input("Enter class: ")
                roll_number = int(input("Enter roll number: "))

                student_count += 1

                print("\nStudent added successfully.")
                print(f"Name       : {name}")
                print(f"Age        : {age}")
                print(f"Class      : {class_name}")
                print(f"Roll Number: {roll_number}")

            elif student_choice == 2:
                if student_count == 0:
                    print("No student information available.")

                else:
                    print("\n========== STUDENT INFORMATION ==========")
                    print("Student records are currently available.")
                    print(f"Total Students Added: {student_count}")

            elif student_choice == 3:
                search_roll = int(input("Enter roll number to search: "))

                if student_count > 0:
                    print(f"Searching for roll number {search_roll}...")
                    print("Student search completed.")

                else:
                    print("No students available.")

            elif student_choice == 4:
                break

            else:
                print("Invalid choice.")

    # Teacher management.
    elif choice == 2:

        while True:
            print("\n========== TEACHER MANAGEMENT ==========")
            print("1. Add Teacher")
            print("2. View Teacher Information")
            print("3. Back")
            print("========================================")

            teacher_choice = int(input("Enter your choice: "))

            if teacher_choice == 1:
                teacher_name = input("Enter teacher name: ")
                subject = input("Enter subject: ")
                experience = int(input("Enter experience in years: "))

                teacher_count += 1

                print("\nTeacher added successfully.")
                print(f"Name       : {teacher_name}")
                print(f"Subject    : {subject}")
                print(f"Experience : {experience} years")

            elif teacher_choice == 2:
                print("\n========== TEACHER INFORMATION ==========")

                if teacher_count == 0:
                    print("No teacher records available.")

                else:
                    print(f"Total Teachers: {teacher_count}")

            elif teacher_choice == 3:
                break

            else:
                print("Invalid choice.")

    # Attendance management.
    elif choice == 3:

        while True:
            print("\n========== ATTENDANCE ==========")
            print("1. Mark Attendance")
            print("2. Attendance Summary")
            print("3. Back")
            print("================================")

            attendance_choice = int(input("Enter your choice: "))

            if attendance_choice == 1:
                student = input("Enter student name: ")

                day = 1
                present = 0
                absent = 0

                print("\nEnter attendance for 5 days.")

                while day <= 5:
                    status = input(f"Day {day} - Present or Absent (P/A): ").upper()

                    if status == "P":
                        present += 1
                        day += 1

                    elif status == "A":
                        absent += 1
                        day += 1

                    else:
                        print("Invalid input. Enter P or A.")

                attendance_percentage = present / 5 * 100

                print("\n========== ATTENDANCE REPORT ==========")
                print(f"Student   : {student}")
                print(f"Present   : {present}")
                print(f"Absent    : {absent}")
                print(f"Attendance: {attendance_percentage:.2f}%")
                print("=======================================")

            elif attendance_choice == 2:
                print("\nAttendance summary can be viewed after marking attendance.")

            elif attendance_choice == 3:
                break

            else:
                print("Invalid choice.")

    # Marks and result management.
    elif choice == 4:

        while True:
            print("\n========== MARKS & RESULT ==========")
            print("1. Calculate Result")
            print("2. Back")
            print("====================================")

            result_choice = int(input("Enter your choice: "))

            if result_choice == 1:
                student_name = input("Enter student name: ")

                subject_number = 1
                total = 0
                failed = 0

                # Enter marks for five subjects.
                while subject_number <= 5:

                    if subject_number == 1:
                        subject = "Mathematics"

                    elif subject_number == 2:
                        subject = "English"

                    elif subject_number == 3:
                        subject = "Science"

                    elif subject_number == 4:
                        subject = "Computer"

                    else:
                        subject = "Hindi"

                    marks = float(input(f"Enter marks in {subject}: "))

                    if marks < 40:
                        failed += 1

                    total += marks
                    subject_number += 1

                percentage = total / 5

                if failed > 0:
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

                print("\n========== RESULT ==========")
                print(f"Student    : {student_name}")
                print(f"Total      : {total}/500")
                print(f"Percentage : {percentage:.2f}%")
                print(f"Grade      : {grade}")
                print(f"Result     : {result}")
                print("============================")

            elif result_choice == 2:
                break

            else:
                print("Invalid choice.")

    # Fee management.
    elif choice == 5:

        while True:
            print("\n========== FEE MANAGEMENT ==========")
            print("1. Calculate Fee")
            print("2. Pay Fee")
            print("3. Fee Status")
            print("4. Back")
            print("====================================")

            fee_choice = int(input("Enter your choice: "))

            if fee_choice == 1:
                student = input("Enter student name: ")
                annual_fee = float(input("Enter annual fee: ₹"))
                paid_fee = float(input("Enter already paid fee: ₹"))

                remaining_fee = annual_fee - paid_fee

                if remaining_fee <= 0:
                    status = "Fully Paid"
                    remaining_fee = 0

                elif paid_fee > 0:
                    status = "Partially Paid"

                else:
                    status = "Not Paid"

                print("\n========== FEE STATUS ==========")
                print(f"Student       : {student}")
                print(f"Annual Fee    : ₹{annual_fee:.2f}")
                print(f"Paid Fee      : ₹{paid_fee:.2f}")
                print(f"Remaining Fee : ₹{remaining_fee:.2f}")
                print(f"Status        : {status}")
                print("===============================")

            elif fee_choice == 2:
                payment = float(input("Enter fee payment: ₹"))

                if payment <= 0:
                    print("Invalid payment.")

                else:
                    total_fees += payment
                    print(f"Payment of ₹{payment:.2f} received.")

            elif fee_choice == 3:
                print(f"\nTotal fees collected: ₹{total_fees:.2f}")

            elif fee_choice == 4:
                break

            else:
                print("Invalid choice.")

    # School report.
    elif choice == 6:

        print("\n======================================")
        print("           SCHOOL REPORT")
        print("======================================")
        print(f"Students Added : {student_count}")
        print(f"Teachers Added : {teacher_count}")
        print(f"Fees Collected : ₹{total_fees:.2f}")
        print("School Status  : Active")
        print("======================================")

    # Exit the program.
    elif choice == 7:
        print("\n======================================")
        print("       SCHOOL SYSTEM CLOSED")
        print("======================================")
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Please try again.")
