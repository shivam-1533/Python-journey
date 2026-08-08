#  WAP TO DISPLAY WEEKDAY FROM NUMBER 
#  INPUT A NUMBER (1 TO 7) AND DISPLAY THE CORRESPONDING WEEKDAY. 


name = input("ENTER YOUR NAME:  ")

day = int(input("ENTER THE DAY NUMBER BETWEEN 1 AND 7:  "))

if day > 7 :
    print("THIS IS THE WRONG INPUT YOUR CRITERIA IS 1 TO 7 THANK YOU🥰")

elif day == 1 :
    print(day,'IS "MONDAY" TODAY IS WORKING DAY FOR YUHH👨‍💻')

    
elif day == 2 :
    print(day,'IS "TUESDAY" TODAY IS WORKING DAY FOR YUHH👨‍💻')

elif day == 3 :
    print(day,'IS "WEDNESDAY" TODAY IS WORKING DAY FOR YUHH👨‍💻')

elif day == 4 :
    print(day,'IS "THURSDAY" TODAY IS WORKING DAY FOR YUHH👨‍💻')

elif day == 5 :
    print(day,'IS "FRIDAY" TODAY IS WORKING DAY FOR YUHH👨‍💻')

elif day == 6 :
    print(day,'IS "SATURDAY" TODAY IS WEEKEND DAY FOR YUHH ENJOY 🍾')

elif day == 7 :
    print(day,'IS "SUNDAY" TODAY IS WEEKOFF FOR YOUHH 🧘')

print(name,"THANK YOU FOR VISITING 🙏")