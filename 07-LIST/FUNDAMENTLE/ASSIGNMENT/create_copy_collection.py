# ============================================================
#                    COPY OF LIST
# ============================================================


n = int(input("\nENTER THE NUMBER OF ELEMENTS: "))

numbers = []


print("\n" + "-" * 60)
print("              ENTER LIST ELEMENTS")
print("-" * 60)

for index in range(n):
    element = input(f"ENTER ELEMENT AT INDEX {index}: ")
    numbers.append(element)


copy_list = numbers.copy()


print("\n" + "=" * 60)
print("                 ORIGINAL LIST")
print("=" * 60)

print(f"\nORIGINAL LIST : {numbers}")


print("\n" + "=" * 60)
print("                   COPY LIST")
print("=" * 60)

print(f"\nCOPY LIST     : {copy_list}")


print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
