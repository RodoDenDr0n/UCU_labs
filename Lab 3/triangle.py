base = int(input())
height = int(input())

for i in range(height):
    for j in range(height-i):
        if j == height - i - 1:
            print(base + j, end="")
            break
        print(base + j, end=" ")
    print()