#  Wrote a program to calculate compound interest.

P = float(input("ENTER PRINCIPAL AMMOUNT OF YOUR LOAN: "))
R = float(input("ENTER INTEREST RATE OF YOUR LOAN: "))
T = float(input("ENTER TIME OF YOUR LOAN: "))
N = float(input("ENTER YEARLY INTEREST RATE ADD IN YOU LOAN: "))

C_I = P * (1 + (R / 100 * N)) ** (N * T)

print(C_I)