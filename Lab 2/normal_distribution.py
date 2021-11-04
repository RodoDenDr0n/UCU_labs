import math

x = float(input())
m = float(input())
o = float(input())
num = ((-1)*((x-m)**2))/(2*o**2)

func = (1/math.sqrt(2*math.pi*o**2)) * math.exp(num)

print(round(func, 10))