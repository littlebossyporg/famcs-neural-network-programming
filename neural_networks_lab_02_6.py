#  a) Определите: сколько гласных и сколько согласных букв в строке.

print("Ввведите строку (en) : ")
origin_string = input()
counter = 0
symbols = 0
for i in range(len(origin_string)):
    if origin_string[i] != " " and origin_string[i]!=" ":
        if origin_string[i] in 'AEIOUYaeiouy':
            counter += 1
    else:
        symbols += 1
print("Глсных : " + str(counter) + ", согласных : " + str(len(origin_string) - counter - symbols))

#  b) Дано предложение, слова которого отделены пробелами, в конце предложения точка.
#  Напишите каждое слово, начиная его с большой буквы и заканчивая точкой.

print("Ввведите предложение, слова которого отделены пробелами, в конце предложения точка : ")
origin_string = input()
words_list = origin_string.replace('.', '').split()
for word in words_list:
    print(str(word[:1]).upper() + word[1:], end=". ")
print(end="\n")

# c) Дана строка. Определите частоту, с которой входят разные буквы в эту строку.

print("Ввведите строку : ")
origin_string = input()
dictionary = {}
for i in range(len(origin_string)):
    if origin_string[i] != " " and origin_string[i] != ".":
        if dictionary.setdefault(origin_string[i]) is None:
            dictionary[origin_string[i]] = 1
        else:
            dictionary[origin_string[i]] = dictionary.setdefault(origin_string[i]) + 1
print(dictionary)

#  d) Дана строка. Группы символов между пробелами считаются словами.
#  Определите сколько слов начинается и заканчивается одной и той же буквой.

print("Ввведите строку : ")
origin_string = input()
words_list = origin_string.split()
counter = 0
for word in words_list:
    if word[0] == word[len(word) - 1]:
        counter += 1
print(str(counter) + " слов начинается и заканчивается одной и той же буквой")

#  В списке перепишите все ненулевые элементы в начало списка (сохраняя порядок),
#  а нулевые - в конец.

print("Ввведите элементы списка через пробел : ")
origin_list = [int(i) for i in input().split()]
counter = 0
origin_list.sort(key=lambda val: val == 0)
print(origin_list)

#  g) Получите список из положительных элементов другого списка, стоящих на четных местах.

print("Ввведите элементы списка через пробел : ")
origin_list = [int(i) for i in input().split()]
list_of_positive_elements = []
for i in range(len(origin_list)):
    if i % 2 == 0 and origin_list[i] > 0:
        list_of_positive_elements.append(origin_list[i])
print(list_of_positive_elements)
