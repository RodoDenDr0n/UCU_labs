x, y = input("Enter two values: ").split() #str
hemming_distance = 0

x1 = bin(int(x))[2:]

for i in range(len(x1)):
    if ((int(x) >> i) & 1) ^ ((int(y) >> i) & 1) == True:
        hemming_distance += 1

print(hemming_distance)