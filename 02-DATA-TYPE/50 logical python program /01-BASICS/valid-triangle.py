# Check whether three sides can form a valid triangle.

side_a = float(input("ENTER THE FIRST SIDE OF TRIANGLE: "))
side_b = float(input("ENTER THE SECOND SIDE OF TRIANGLE: "))
side_c = float(input("ENTER THE THIRD SIDE OF TRIANGLE: "))

if side_a == side_b and side_b == side_c:
    print("THIS IS A VALID 'TRIANGLE'")

else:
    print("THIS IS NOT A VALID TRIANGLE")
