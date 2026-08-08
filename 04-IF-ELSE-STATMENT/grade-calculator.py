# Calculate the grade based on the marks obtained.

# Take the student's marks as input.
marks = int(input("Enter marks: "))

# Determine the grade based on the marks.
if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")
