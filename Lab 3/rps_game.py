result = []

for i in range(10):
    game = input()
    if game == "SP" or game == "PR" or game == "RS":
        result.append("True")
    elif game == "PS" or game == "RP" or game == "SR":
        result.append("False")
    elif game == "":
        break
    else:
        result.append("False | False")

for i in range(len(result)):
    print(result[i])
