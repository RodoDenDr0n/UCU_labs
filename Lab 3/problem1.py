a = int(input())

if a > 3:
    print("*")
    for i in range(a - 2):
        print("*" + " "*(i) + "*")
        if i == a-3: 
            print("*"*(i+3))
else:
    for i in range(1, a+1):
        print("*"*i)

# for i in range(a-2):
#     if a > 3:
#         print("*" + " "*(i) + "*") 
#         if i == a-3:
#             print("*"*(i))
#     else:
#         print("*"*(i))