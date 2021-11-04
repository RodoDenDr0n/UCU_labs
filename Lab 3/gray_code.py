user_number1 = input()
num = int(user_number1, 2)
grey_number = ""

user_number2 = bin(num >> 1)[2:].zfill(len(user_number1))

for i in range(len(user_number2)):
    if int(user_number1[i]) ^ int(user_number2[i]) == True:
        grey_number += "1"
    else:
        grey_number += "0"
        
print(grey_number)