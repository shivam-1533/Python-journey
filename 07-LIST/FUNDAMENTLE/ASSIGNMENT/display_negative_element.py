# ============================================================
#              NEGATIVE NUMBERS FROM LIST
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


print("\n" + "=" * 60)
print("               NEGATIVE NUMBERS")
print("=" * 60)

for negative in numbers:
    if negative < 0:
        print(negative)


print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
