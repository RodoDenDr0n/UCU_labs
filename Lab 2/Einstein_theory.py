import math

c = 299792458
m = float(input())
v = float(input())

mr = m/(math.sqrt(1 - (v/c)**2))
E = mr * c**2

print(E)