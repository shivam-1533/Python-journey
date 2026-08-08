# Display a message based on the student's grade.

# Take the grade as input and convert it to uppercase.
grade = input("Enter grade (A/B/C/D/F): ").upper()

# Display the result based on the entered grade.
match grade:
    case "A":
        print("Excellent")

    case "B":
        print("Very Good")

    case "C":
        print("Good")

    case "D":
        print("Pass")

    case "F":
        print("Fail")

    case _:
        print("Invalid grade.")
