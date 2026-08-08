#  Determine the age category: Child, Teenager, Adult, Senior Citizen.

age = int(input("ENTER YOU AGE: "))

# logic for age criteria 

if age <= 8:
    print('YOU ARE "CHILDREN"')
elif age >=8 and age <= 21:
    print('"YOU ARE "TEENAGER"')
elif age >= 21 and age <= 60:
    print('YOU ARE "ADULT"')

else:
    print('YOU ARE SENIOU "CETZEN"')