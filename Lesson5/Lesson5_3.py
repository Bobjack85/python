# Задача-3:
'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 200, вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
firm = {'Red': 100, 'Pink': 150, 'Black': 200, 'Green': 250}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"averate: {result}")
