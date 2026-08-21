# ============================================================
#                 COUNT EACH ELEMENT
# ============================================================


n = int(input("\nENTER THE NUMBER OF ELEMENTS: "))

numbers = []


print("\n" + "-" * 60)
print("              ENTER LIST ELEMENTS")
print("-" * 60)

for index in range(n):
    element = input(f"ENTER ELEMENT AT INDEX {index}: ")
    numbers.append(element)


print("\n" + "=" * 60)
print("                 YOUR LIST")
print("=" * 60)

print(f"\nCOLLECTION : {numbers}")


visited = []


for x in numbers:

    if x not in visited:

        count = 0

        for y in numbers:
            if x == y:
                count += 1

        visited.append(x)


print("\n" + "=" * 60)
print("                ELEMENT COUNT")
print("=" * 60)

for x in visited:

    count = 0

    for y in numbers:
        if x == y:
            count += 1

    print(f"{x:<15} : {count}")


print("\n" + "=" * 60)
print("                 PROGRAM END")
print("=" * 60)
