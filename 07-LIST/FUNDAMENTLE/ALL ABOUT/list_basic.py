# ============================================================
#                       PYTHON LIST
# ============================================================
# List kya hoti hai?
# List ek aisa data structure hai jisme hum multiple values
# ko ek hi variable mein store kar sakte hain.
#
# List mein hum:
# - Items ko access kar sakte hain
# - Items ko change kar sakte hain
# - New items add kar sakte hain
# - Items remove kar sakte hain
# - List ko sort kar sakte hain
# - List par loop chala sakte hain
# - List comprehension ka use kar sakte hain
# ============================================================


# ------------------------------------------------------------
# 1. List Create Karna Aur Print Karna
# ------------------------------------------------------------
# Yahan hum ek fruits naam ki list bana rahe hain.
# List ke andar multiple fruits store kiye gaye hain.
# print() ki madad se hum poori list ko display kar rahe hain.

print("=" * 60)
print("             1. LIST CREATE KARNA")
print("=" * 60)

fruits = ["apple", "banana", "mango", "orange"]

print("\nList:")
print(fruits)


# ------------------------------------------------------------
# 2. List Indexing
# ------------------------------------------------------------
# Indexing ka use list ke kisi particular item ko access
# karne ke liye kiya jata hai.
#
# Python mein indexing 0 se start hoti hai:
# apple  -> 0
# banana -> 1
# mango  -> 2
# orange -> 3
#
# Negative indexing mein:
# -1 = last item
# -2 = second last item

print("\n" + "=" * 60)
print("             2. LIST INDEXING")
print("=" * 60)

print("\nIndex 2 ka item:")
print(fruits[2])

print("\nLast item:")
print(fruits[-1])


# ------------------------------------------------------------
# 3. List Ke Item Ko Change Karna
# ------------------------------------------------------------
# List mutable hoti hai.
# Mutable ka matlab hai ki list banne ke baad bhi hum
# uske existing items ko change kar sakte hain.
#
# Yahan index 2 par "mango" ko "grapes" se replace kiya gaya hai.

print("\n" + "=" * 60)
print("             3. LIST ITEM CHANGE KARNA")
print("=" * 60)

fruits[2] = "grapes"

print("\nUpdated List:")
print(fruits)


# ------------------------------------------------------------
# 4. List Mein Item Add Karna - append()
# ------------------------------------------------------------
# append() method list ke END mein ek new item add karta hai.
#
# Yahan "pineapple" ko list ke end mein add kiya gaya hai.

print("\n" + "=" * 60)
print("             4. append() METHOD")
print("=" * 60)

fruits.append("pineapple")

print("\nUpdated List:")
print(fruits)


# ------------------------------------------------------------
# 5. Specific Position Par Item Add Karna - insert()
# ------------------------------------------------------------
# insert() method kisi specific index par item add karta hai.
#
# Syntax:
# list.insert(index, item)
#
# Yahan index 1 par "red" add kiya gaya hai.

print("\n" + "=" * 60)
print("             5. insert() METHOD")
print("=" * 60)

fruits.insert(1, "red")

print("\nUpdated List:")
print(fruits)


# ------------------------------------------------------------
# 6. Doosri List Ke Multiple Items Add Karna - extend()
# ------------------------------------------------------------
# extend() method ek list ke saare items ko doosri list
# ke end mein add karta hai.
#
# Yahan list 'b' ke items ko list 'a' mein add kiya gaya hai.

print("\n" + "=" * 60)
print("             6. extend() METHOD")
print("=" * 60)

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)

print("\nList A:")
print(a)


# ------------------------------------------------------------
# 7. List Se Item Remove Karna - remove()
# ------------------------------------------------------------
# remove() method kisi particular VALUE ko list se remove karta hai.
#
# Yahan "apple" value ko list se remove kiya gaya hai.

print("\n" + "=" * 60)
print("             7. remove() METHOD")
print("=" * 60)

print("\nOriginal List:")
print(fruits)

fruits.remove("apple")

print("\nUpdated List:")
print(fruits)


# ------------------------------------------------------------
# 8. List Se Item Remove Karna - pop()
# ------------------------------------------------------------
# pop() method kisi index ke item ko remove karta hai.
# Saath hi removed item ko return bhi karta hai.
#
# Yahan index 1 ka item remove kiya gaya hai.

print("\n" + "=" * 60)
print("             8. pop() METHOD")
print("=" * 60)

fruits = ["apple", "banana", "mango"]

removed_item = fruits.pop(1)

print("\nRemoved Item:")
print(removed_item)

print("\nUpdated List:")
print(fruits)


# ------------------------------------------------------------
# 9. List Se Item Delete Karna - del
# ------------------------------------------------------------
# del keyword ka use kisi particular index ke item ko
# delete karne ke liye kiya ja sakta hai.
#
# Yahan index 1 ka item delete kiya gaya hai.

print("\n" + "=" * 60)
print("             9. del KEYWORD")
print("=" * 60)

fruits = ["apple", "banana", "mango"]

del fruits[1]

print("\nUpdated List:")
print(fruits)


# ------------------------------------------------------------
# 10. List Ke Saare Items Remove Karna - clear()
# ------------------------------------------------------------
# clear() method list ke saare items ko remove kar deta hai.
# List delete nahi hoti, balki empty list ban jati hai.

print("\n" + "=" * 60)
print("             10. clear() METHOD")
print("=" * 60)

fruits = ["apple", "banana", "mango"]

fruits.clear()

print("\nList after clear():")
print(fruits)


# ------------------------------------------------------------
# 11. List Mein Item Check Karna - in
# ------------------------------------------------------------
# 'in' operator check karta hai ki koi particular item
# list ke andar present hai ya nahi.
#
# Item present hone par True return hota hai.
# Item present na hone par False return hota hai.

print("\n" + "=" * 60)
print("             11. 'in' OPERATOR")
print("=" * 60)

fruits = ["apple", "banana", "mango"]

print("\n'banana' list mein hai?:", "banana" in fruits)
print("'pineapple' list mein hai?:", "pineapple" in fruits)


# ------------------------------------------------------------
# 12. List Par for Loop Chalana
# ------------------------------------------------------------
# for loop list ke har item ko ek-ek karke access karta hai.
#
# Yahan loop fruits list ke har fruit ko print karega.

print("\n" + "=" * 60)
print("             12. FOR LOOP")
print("=" * 60)

fruits = ["apple", "banana", "mango"]

print()

for fruit in fruits:
    print("🍎", fruit)


# ------------------------------------------------------------
# 13. Index Aur Item Dono Print Karna - enumerate()
# ------------------------------------------------------------
# enumerate() ka use tab hota hai jab hume list ke item
# ke saath uska index bhi chahiye.
#
# enumerate() do values provide karta hai:
# 1. Index
# 2. Item

print("\n" + "=" * 60)
print("             13. enumerate()")
print("=" * 60)

fruits = ["apple", "banana", "mango"]

print()

for index, fruit in enumerate(fruits):
    print(f"Index {index}  ->  {fruit}")


# ============================================================
#                       SORTING
# ============================================================
# Sorting ka matlab list ke items ko ek particular order
# mein arrange karna hota hai.
#
# sort() default mein ascending order mein sort karta hai.
# sort(reverse=True) descending order mein sort karta hai.
# ============================================================


# ------------------------------------------------------------
# 14. List Ko Ascending Order Mein Sort Karna
# ------------------------------------------------------------
# sort() method list ko smallest se largest order mein
# arrange karta hai.

print("\n" + "=" * 60)
print("             14. SORTING - ASCENDING")
print("=" * 60)

numbers = [4, 5, 2, 5, 1, 8, 11, 10, 8, 3]

numbers.sort()

print("\nAscending Order:")
print(numbers)


# ------------------------------------------------------------
# 15. List Ko Descending Order Mein Sort Karna
# ------------------------------------------------------------
# sort(reverse=True) list ko largest se smallest order
# mein arrange karta hai.

print("\n" + "=" * 60)
print("             15. SORTING - DESCENDING")
print("=" * 60)

numbers.sort(reverse=True)

print("\nDescending Order:")
print(numbers)


# ------------------------------------------------------------
# 16. count() Aur index() Methods
# ------------------------------------------------------------
# count() kisi value ke list mein total occurrences
# count karta hai.
#
# index() kisi value ka first index return karta hai.

print("\n" + "=" * 60)
print("             16. count() AUR index()")
print("=" * 60)

numbers = [10, 20, 10, 30, 10]

print("\n10 kitni baar hai?:", numbers.count(10))
print("10 ka first index:", numbers.index(10))


# ------------------------------------------------------------
# 17. Do Lists Ko + Operator Se Combine Karna
# ------------------------------------------------------------
# '+' operator ka use do lists ko combine karne ke liye
# kiya ja sakta hai.
#
# Isse ek new list create hoti hai.

print("\n" + "=" * 60)
print("             17. LIST CONCATENATION")
print("=" * 60)

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print("\nCombined List:")
print(c)


# ------------------------------------------------------------
# 18. List Ko Multiple Times Repeat Karna
# ------------------------------------------------------------
# '*' operator ka use list ko multiple times repeat
# karne ke liye kiya ja sakta hai.
#
# Yahan [1, 2] ko 3 times repeat kiya gaya hai.

print("\n" + "=" * 60)
print("             18. LIST REPETITION")
print("=" * 60)

numbers = [1, 2]

print("\nRepeated List:")
print(numbers * 3)


# ============================================================
#                       NESTED LIST
# ============================================================
# Nested list ka matlab hai ek list ke andar doosri lists.
#
# Example:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# Iska use matrix ya table jaise data ko represent karne
# ke liye kiya ja sakta hai.
# ============================================================


# ------------------------------------------------------------
# 19. Nested List
# ------------------------------------------------------------
# matrix ek nested list hai.
#
# matrix[0] -> first row
# matrix[1][2] -> second row ka third item

print("\n" + "=" * 60)
print("             19. NESTED LIST")
print("=" * 60)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nFirst Row:")
print(matrix[0])

print("\nSecond Row ka Third Item:")
print(matrix[1][2])


# ============================================================
#                  LIST COMPREHENSION
# ============================================================
# List comprehension ka use short aur clean way mein
# new list create karne ke liye kiya jata hai.
#
# Basic syntax:
#
# [expression for item in list]
# ============================================================


# ------------------------------------------------------------
# 20. Normal for Loop Se Squares Create Karna
# ------------------------------------------------------------
# Yahan normal for loop ka use karke har number ka square
# calculate karke new list mein add kiya ja raha hai.

print("\n" + "=" * 60)
print("             20. NORMAL FOR LOOP")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num**2)

print("\nSquares:")
print(squares)


# ------------------------------------------------------------
# 21. List Comprehension Se Squares Create Karna
# ------------------------------------------------------------
# Same kaam list comprehension se short form mein
# kiya ja sakta hai.
#
# num ** 2 har number ka square calculate karta hai.

print("\n" + "=" * 60)
print("             21. LIST COMPREHENSION")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

squares = [num**2 for num in numbers]

print("\nSquares:")
print(squares)


# ------------------------------------------------------------
# 22. List Comprehension With Condition
# ------------------------------------------------------------
# List comprehension mein condition bhi lagayi ja sakti hai.
#
# Yahan sirf even numbers ko new list mein store kiya gaya hai.
#
# num % 2 == 0 ka matlab:
# Number ko 2 se divide karne par remainder 0 hona chahiye.

print("\n" + "=" * 60)
print("             22. COMPREHENSION WITH CONDITION")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6]

even = [num for num in numbers if num % 2 == 0]

print("\nEven Numbers:")
print(even)


# ------------------------------------------------------------
# 23. if-else Ke Saath List Comprehension
# ------------------------------------------------------------
# Yahan har number ko check kiya ja raha hai.
#
# Agar number even hai -> "Even"
# Agar number odd hai  -> "Odd"

print("\n" + "=" * 60)
print("             23. COMPREHENSION WITH if-else")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

print("\nResult:")
print(result)


# ============================================================
#                       map()
# ============================================================
# map() ka use kisi function ko list ke har item par
# apply karne ke liye kiya jata hai.
#
# Yahan lambda function har number ka square calculate
# kar raha hai.
# ============================================================


# ------------------------------------------------------------
# 24. map() + lambda
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("             24. map() + lambda")
print("=" * 60)

numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x**2, numbers))

print("\nSquares:")
print(squares)


# ============================================================
#                       filter()
# ============================================================
# filter() ka use list mein se sirf un items ko select
# karne ke liye kiya jata hai jo given condition ko satisfy
# karte hain.
#
# Yahan sirf even numbers select kiye ja rahe hain.
# ============================================================


# ------------------------------------------------------------
# 25. filter() + lambda
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("             25. filter() + lambda")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print("\nEven Numbers:")
print(even)


# ============================================================
#                         any()
# ============================================================
# any() check karta hai ki iterable mein kam se kam
# ek condition True hai ya nahi.
#
# Agar ek bhi value True hoti hai to any() -> True return karta hai.
# ============================================================


# ------------------------------------------------------------
# 26. any() Function
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("             26. any() FUNCTION")
print("=" * 60)

numbers = [1, 3, 5, 8]

result = any(num % 2 == 0 for num in numbers)

print("\nKya koi Even Number hai?:")
print(result)


# ============================================================
#                         all()
# ============================================================
# all() check karta hai ki iterable ke ALL items condition
# ko satisfy karte hain ya nahi.
#
# Agar sabhi values True hoti hain to all() -> True return karta hai.
# ============================================================


# ------------------------------------------------------------
# 27. all() Function
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("             27. all() FUNCTION")
print("=" * 60)

numbers = [2, 4, 6, 8]

result = all(num % 2 == 0 for num in numbers)

print("\nKya Saare Numbers Even Hain?:")
print(result)


# ============================================================
#                       COPY
# ============================================================
# List ko copy karne ke liye copy() aur deepcopy() ka
# use kiya ja sakta hai.
#
# copy() -> shallow copy
# deepcopy() -> nested objects ki bhi independent copy
#
# Nested lists ke case mein deepcopy() useful hota hai.
# ============================================================


# ------------------------------------------------------------
# 28. Shallow Copy - copy()
# ------------------------------------------------------------
# copy() method list ki ek shallow copy create karta hai.

print("\n" + "=" * 60)
print("             28. SHALLOW COPY")
print("=" * 60)

a = [[1, 2], [3, 4]]

b = a.copy()

print("\nOriginal List:")
print(a)

print("\nCopied List:")
print(b)


# ------------------------------------------------------------
# 29. Deep Copy - deepcopy()
# ------------------------------------------------------------
# deepcopy() nested list ke andar ke objects ki bhi
# independent copy create karta hai.
#
# Iske liye Python ke copy module se deepcopy import karna hota hai.

print("\n" + "=" * 60)
print("             29. DEEP COPY")
print("=" * 60)

import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

print("\nOriginal List:")
print(a)

print("\nDeep Copied List:")
print(b)


# ============================================================
#                         zip()
# ============================================================
# zip() ka use multiple lists ke corresponding items ko
# ek saath combine karke iterate karne ke liye kiya jata hai.
#
# Yahan:
# names -> students ke names
# marks -> students ke marks
#
# zip() same position ke name aur mark ko pair karta hai.
# ============================================================


# ------------------------------------------------------------
# 30. zip() Function
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("             30. zip() FUNCTION")
print("=" * 60)

names = ["Aman", "Rahul", "Vikas"]
marks = [80, 90, 75]

print()

for name, mark in zip(names, marks):
    print(f"Name: {name:<10} | Marks: {mark}")


# ============================================================
#                         END
# ============================================================

print("\n" + "=" * 60)
print("              PYTHON LIST COMPLETE")
print("=" * 60)
print("       Total Concepts Covered: 30")
print("=" * 60)
