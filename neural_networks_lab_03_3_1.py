#  a) По аналогии с разобранным примером составьте список фамилий группы и запишите его в текстовый файл.
#  Распечатайте созданный файл.

list_of_students = []
file = open('surnames.txt', 'w')
print("Введите фамилию студента (чтобы закончить ввод фамилий введите stop) : ")
surname = input()
while surname != "stop":
    print("Введите фамилию студента (чтобы закончить ввод фамилий введите stop) : ")
    list_of_students.append(surname + "\n")
    surname = input()
file.writelines(list_of_students)
file.close()
file = open('surnames.txt', 'r')
print(file.read())
file.close()

#  b) Распечатайте созданный файл фамилий построчно, добавив перед каждой
#  фамилией ее порядковый номер.

file = open('surnames.txt', 'r')
counter = 1
for line in file:
    print(str(counter) + ")", line[:-1])
    counter += 1
file.close()

#  c) Создайте файл, добавив к каждой фамилии имя. Распечатайте его построчно.

counter = 1
for i in range(len(list_of_students)):
    print("Введите имя студента", counter, ":")
    list_of_students[i] = list_of_students[i][:-1] + " " + input() + "\n"
    counter += 1
file = open('surnames.txt', 'w')
file.writelines(list_of_students)
file.close()
file = open('surnames.txt', 'r')
print(file.read())
file.close()

#  d) Распечатайте из последнего файла только фамилию и первую букву имени.

file = open('surnames.txt', 'r')
for line in file:
    surname, name = line.split()
    print(surname, name[0])
file.close()
