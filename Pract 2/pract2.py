import random

num = int(input("Введіть кількість чисел, яку бажаєте згенерувати: "))
diapason = int(input("Введіть діапазон чисел: "))
num_list = []
command_list = ["prime", "comp"]



for i in range(num):
    random_number = random.randrange(diapason)
    num_list.append(random_number)
print("Ваш спсок згенерованих чисел: ", num_list)
print("Випадково обране число: ", random.choice(num_list))

