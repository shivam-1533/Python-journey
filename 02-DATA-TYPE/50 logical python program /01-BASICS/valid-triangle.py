# Check whether three sides can form a valid triangle.

# Take the three side lengths as input from the user.
side_a = float(input("Enter the first side of the triangle: "))
side_b = float(input("Enter the second side of the triangle: "))
side_c = float(input("Enter the third side of the triangle: "))

# Check the triangle inequality condition.
if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
    print("These sides can form a valid triangle.")
else:
    print("These sides cannot form a valid triangle.")
