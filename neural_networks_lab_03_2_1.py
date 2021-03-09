#  a) Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
#  вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и
#  выведите результат работы этой функции.
import math


def distance(x1_, y1_, x2_, y2_):
    return math.sqrt(math.pow(x1_ - x2_, 2) + math.pow(y1_ - y2_, 2))


print("Введите координаты точек x1, y1, x2, y2 : ")
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print("Расстояние :", distance(x1, x2, y1, y2))


#  b) Дано действительное положительное число a и целоe число n.
#  Вычислите a^n. Решение оформите в виде функции power(a, n).
#  Стандартной функцией возведения в степень можно пользоваться для проверки результата.

def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    if n < 0:
        return 1 / result
    return result


print("Введите число и стпень, в которую его возвести : ")
print("Результат :", power(float(input()), int(input())))


#  c) Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает
#  его же, меняя первую букву на большую.
#  Например, print(capitalize('word')) должно печатать слово Word.
#  На вход подаётся строка, состоящая из слов, разделённых одним пробелом.
#  Слова состоят из маленьких латинских букв. Напечатайте исходную строку, сделав так,
#  чтобы каждое слово начиналось с большой буквы. При этом используйте вашу функцию capitalize().
#  Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII,
#  и функция chr(), которая по коду символа возвращает сам символ. Например, ord('a') == 97,
#  chr(97) == 'a'.

def capitalize(original_word):
    original_letter = original_word[0]
    transformed_letter = chr(ord(original_letter) - ord('a') + ord('A'))
    return transformed_letter + original_word[1:]


print("Введите строку (en) : ")
words = input().split()
for word in words:
    print(capitalize(word), end=" ")
print(end="\n")


# d) Напишем функцию max(), которая принимает переменное число аргументов и возвращает максимум из
# них (на самом деле, такая функция уже встроена в Питон).

def custom_max(*arguments_list):  # в уссловии было просто max, но лучше,
    result = arguments_list[0]  # если название не совпадает со встроеными функциями
    for value in arguments_list:
        if value > result:
            result = value
    return result


print("Введите числа среди которых нужно найти максимум (через пробел) :")
numbers = [int(i) for i in input().split()]
print(custom_max(*numbers))


#  e) В написанную в пункте a) программу добавьте обработку не менее двух типов исключений.

class ZeroDistanceError(Exception):
    def __init__(self, message):
        self.txt = message


try:
    print("Введите координаты точек x1, y1, x2, y2 : ")
    x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
    if x1 == x2 and y1 == y2:
        raise ZeroDistanceError("Вы ввели одну и ту же точку !")
    print("Расстояние :", distance(x1, y1, x2, y2))
except ValueError:
    print("Введены неверные данные !")
except ZeroDistanceError as my_error:
    print(my_error)
