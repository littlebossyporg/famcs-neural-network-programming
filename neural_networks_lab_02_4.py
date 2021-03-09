#  b) Дана строка, состоящая ровно из двух слов, разделенных пробелом.
#  Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
#  При решении этой задачи не стоит пользоваться циклами и инструкцией if.

print("Ввведите строку из двух слов : ")
origin_string = input()
new_string = origin_string[origin_string.find(' ') + 1:] + ' ' + origin_string[:origin_string.find(' ')]
print(new_string)

#  c) Дана строка. Замените в этой строке все цифры 1 на слово one.

print("Ввведите строку, содержащую хотябы одну 1 : ")
print(input().replace('1', 'one'))

#  d) Дана строка, в которой буква h встречается минимум два раза.
#  Удалите из этой строки первое и последнее вхождение буквы h,
#  а также все символы, находящиеся между ними.

origin_string = input()
origin_string = origin_string[:origin_string.find('h')] + origin_string[origin_string.rfind('h') + 1:]
print(origin_string)