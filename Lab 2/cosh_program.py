import math

# cosh(x)= (e**x + e**(-x))/2
x = float(input())

sol1 = math.cosh(x)
sol2 = (math.exp(x) + math.exp(-x))/2
sol3 = (math.e ** x + math.e**(-x))/2

print(f"COS = {sol1:.4f}")
print(f"EXP = {sol2:.4f}")
print(f"E = {sol3:.4f}")

# print("COS =", round(math.cosh(x), 4))
# print("EXP =", round((math.exp(x) + math.exp(-x))/2, 4))
# print("E =", round((math.e ** x + math.e**(-x))/2, 4))