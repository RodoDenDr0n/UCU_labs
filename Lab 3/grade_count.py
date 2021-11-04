grade_list = []
percent_grade = 0
letter_grade = ["A", "B", "C", "D", "E", "F"]

for i in range(5):
    grade = int(input())
    grade_list.append(grade) #введення оцінок в список

for i in range(len(grade_list)):
    if grade_list[i] > 100 or grade_list[i] < 0:
        print(None) # якщо число зі списку буде >100/<0 виведення None
        exit()

for i in range(len(grade_list)):
    percent_grade += grade_list[i] #додавання оцінок зі списку в змінну

percent_grade = percent_grade / len(grade_list) # середнє арифметичне
percent_grade = round(percent_grade, 2) # заокруглення

if percent_grade == 0.0:
    percent_grade = 0

for i in range(len(grade_list)):
    if 90 <= percent_grade <= 100:
        print(f"Average grade = {percent_grade} -> {letter_grade[0]}")
        break

    if 82 <= percent_grade < 90:
        print(f"Average grade = {percent_grade} -> {letter_grade[1]}")
        break

    if 75 <= percent_grade < 82:
        print(f"Average grade = {percent_grade} -> {letter_grade[2]}")
        break

    if 67 <= percent_grade < 75:
        print(f"Average grade = {percent_grade} -> {letter_grade[3]}")
        break

    if 60 <= percent_grade < 67:
        print(f"Average grade = {percent_grade} -> {letter_grade[4]}")
        break

    if 0 <= percent_grade < 60:
        print(f"Average grade = {percent_grade} -> {letter_grade[5]}")
        break