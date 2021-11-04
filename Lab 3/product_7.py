n = int(input())
result = 1

for i in range(0, n+1):
    if i % 7 != 0:
        result *= i

print(result)