# Create a Student Pass/Fail program (Passing marks = 33%).

std_name = input("ENTER STUDENT NAME:  ")
std_rollno = int(input("ENT YOUR ROLL NO: "))
HINDI = int(input("Enter marks Hindi: "))
ENGLISH = int(input("Enter marks English: "))
MATH = int(input("Enter marks Math: "))
SCIENCE = int(input("Enter marks Science: "))
CS = int(input("Enter marks CS: "))

Total_marks = HINDI + ENGLISH + MATH + SCIENCE + CS
Percentage = (Total_marks / 500) * 100

if HINDI > 33 and ENGLISH > 33 and MATH > 33 and SCIENCE > 33 and CS > 33:
    print('Student is "PASS🥰"')

else:
    print('Student is "FAIL😥"')

print("Student Total Marks is: ", Total_marks)
print("Student Total Marks Percentage: ",Percentage)