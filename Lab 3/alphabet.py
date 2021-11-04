alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

number = int(input())
space = " "
height = number

for i in range(0, number):
    print(alphabet[i + (i+1)])
