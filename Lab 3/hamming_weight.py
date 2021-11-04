amount = int(input())
number = 5**amount
number_bit = bin(number)[2:]
hamming_weight = 0

for i in range(len(number_bit)):
    if number_bit[i] == "1":
        hamming_weight += 1

if hamming_weight % 2:
    typus = "odious"
else:  
    typus = "evil"

print(f"Number {number} is {typus} number. Its hamming weight is {hamming_weight}.")