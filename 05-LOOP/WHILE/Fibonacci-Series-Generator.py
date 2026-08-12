#  Fibonacci Series ek aisi number series hoti hai jisme har next number, pichhle do numbers ko add karke banta hai.
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

num = int(input("Enter Number Of Terms :- "))

prev_num = 1

next_num = 0

count = 0

while count < num :
    print(next_num, end=" ")

    c = prev_num + next_num
    prev_num = next_num
    next_num = c

    count += 1