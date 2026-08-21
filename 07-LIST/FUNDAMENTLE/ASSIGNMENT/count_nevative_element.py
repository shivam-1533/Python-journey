# ============================================================
#            POSITIVE & NEGATIVE NUMBER COUNTER
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


negative_count = 0
positive_count = 0


for num in numbers:
    if num < 0:
        negative_count += 1

    if num > 0:
        positive_count += 1


print("\n" + "=" * 60)
print("                 FINAL RESULT")
print("=" * 60)

print(f"\nTOTAL ELEMENTS    : {n}")
print(f"POSITIVE NUMBERS  : {positive_count}")
print(f"NEGATIVE NUMBERS  : {negative_count}")

print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
