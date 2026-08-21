# ============================================================
#              EVEN & ODD NUMBER COUNTER
# ============================================================


n = int(input("\nENTER THE NUMBER OF ELEMENTS: "))

numbers = []


print("\n" + "-" * 60)
print("              ENTER LIST ELEMENTS")
print("-" * 60)

for index in range(n):
    element = int(input(f"ENTER ELEMENT AT INDEX {index}: "))
    numbers.append(element)


print("\n" + "=" * 60)
print("                 YOUR LIST")
print("=" * 60)

print(f"\nCOLLECTION : {numbers}")


even_count = 0
odd_count = 0


for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


print("\n" + "=" * 60)
print("                 FINAL RESULT")
print("=" * 60)

print(f"\nTOTAL ELEMENTS : {n}")
print(f"EVEN NUMBERS   : {even_count}")
print(f"ODD NUMBERS    : {odd_count}")

print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
