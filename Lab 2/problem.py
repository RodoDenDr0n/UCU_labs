import math

r = float(input("Введіть радіус основи циліндра: "))
h = float(input("Введіть висоту циліндра: "))

# V = h * math.pi * pow(r, 2)
# A = h * 2 * math.pi * r + 2 * math.pi * pow(r, 2)

# print(f"V = {V:.3f}")
# print(f"A = {A:.3f}")

V = round(h * math.pi * pow(r, 2), 3)
A = round(h * 2 * math.pi * r + 2 * math.pi * pow(r, 2), 3)

print("V = ", V)
print("A = ", A)