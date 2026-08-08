# Create an online examination system using nested while loops.

print("======================================")
print("        ONLINE EXAMINATION SYSTEM")
print("======================================")

student_name = input("Enter student name: ")
score = 0
question_number = 1

print("\nExam contains 5 questions.")
print("Each correct answer gives 2 marks.")
print("Each wrong answer gives 0 marks.")

# Process each question.
while question_number <= 5:

    print(f"\n========== QUESTION {question_number} ==========")

    if question_number == 1:
        print("What is the output of 2 + 3?")
        print("A. 4")
        print("B. 5")
        print("C. 6")
        print("D. 7")
        correct_answer = "B"

    elif question_number == 2:
        print("Which language are you learning?")
        print("A. Java")
        print("B. C++")
        print("C. Python")
        print("D. PHP")
        correct_answer = "C"

    elif question_number == 3:
        print("Which symbol is used for comments in Python?")
        print("A. //")
        print("B. #")
        print("C. <!-- -->")
        print("D. **")
        correct_answer = "B"

    elif question_number == 4:
        print("Which loop is commonly used when the condition is checked repeatedly?")
        print("A. while")
        print("B. switch")
        print("C. match")
        print("D. import")
        correct_answer = "A"

    else:
        print("What is 10 * 10?")
        print("A. 10")
        print("B. 50")
        print("C. 100")
        print("D. 1000")
        correct_answer = "C"

    # Validate the answer.
    while True:
        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == "A" or answer == "B" or answer == "C" or answer == "D":
            break

        print("Invalid answer. Please enter A, B, C, or D.")

    # Check the answer.
    if answer == correct_answer:
        print("Correct answer! +2 marks")
        score += 2

    else:
        print(f"Wrong answer. Correct answer was {correct_answer}.")

    question_number += 1


# Calculate the final result.
percentage = score / 10 * 100

if percentage >= 90:
    grade = "A+"

elif percentage >= 80:
    grade = "A"

elif percentage >= 70:
    grade = "B"

elif percentage >= 60:
    grade = "C"

elif percentage >= 40:
    grade = "D"

else:
    grade = "F"


print("\n======================================")
print("           EXAM RESULT")
print("======================================")
print(f"Student     : {student_name}")
print(f"Marks       : {score}/10")
print(f"Percentage  : {percentage:.2f}%")
print(f"Grade       : {grade}")
print("======================================")
