amount = int(input())
if amount > 0:
    print('1/2', end = "")

sequence = 3
for i in range(amount-1):
    if i%2 != 0:
        print(' + ', end = "")
    else:
        print(' - ', end = "")
    print(sequence,'/',sequence + 1, sep='', end='')
    sequence += 2
    
print()