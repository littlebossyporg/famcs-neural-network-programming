#  a) Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель,
#  отличный от 1.

print("Введите число для нахождения наименьшего натурального делителя : ")
number = int(input())
smallest_natural_divisor = 2
while number % smallest_natural_divisor != 0:
    smallest_natural_divisor += 1
print("Наименьший натуральный делитель : " + smallest_natural_divisor.__str__())

#  b) В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от
#  предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена
#  составит не менее y километров.

print("Введите сколько пробежал спортсмен в первый день - x  и максимальную дистанцию - y :")
x, y = int(input()), int(input())
day_number = 1
while x < y:
    x *= 1.1
    day_number += 1
print("День номер : " + day_number.__str__())

#  c) Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чего дробная
#  часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее y рублей.
#  Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей,
#  т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.

print("Введите размер вклада, процент, и максимальный размер вклада : ")
x, p, y = int(input()), int(input()), int(input())
number_of_years = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    number_of_years += 1
print("Через " + number_of_years.__str__() + " лет")

# d) Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число
# n, что φn = A. Если А не является числом Фибоначчи, выведите число -1.

fibonachi_number = int(input())
if number == 0:
    print("Число является 0 по счёту ")
else:
    previous_number, next_number = 0, 1
    number_of_fibonachi_number = 1
    while next_number <= fibonachi_number:
        if next_number == fibonachi_number:
            print("Число является " + number_of_fibonachi_number.__str__() + " по счёту ")
            break
        previous_number, next_number = next_number, previous_number + next_number
        number_of_fibonachi_number += 1
    else:
        print(-1)

