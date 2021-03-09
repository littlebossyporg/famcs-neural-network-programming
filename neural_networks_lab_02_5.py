import random

#  b) Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

print("Ввведите элементы списка через пробел : ")
origin_list = [int(i) for i in input().split()]
print("Список : " + str(origin_list))
for i in range(1, len(origin_list)):
    if origin_list[i] > origin_list[i - 1]:
        print(origin_list[i])

#  c) Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей,
#  и выведите количество таких элементов. Крайние элементы списка никогда не учитываются,
#  поскольку у них недостаточно соседей.

origin_list = [random.randint(0, 100) for i in range(10)]
print("Список : " + str(origin_list))
counter = 0
for i in range(1, len(origin_list) - 1):
    if origin_list[i - 1] < origin_list[i] > origin_list[i + 1]:
        counter += 1
print(counter)

#  d) В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

print("Ввведите элементы списка через пробел (элементы должны быть различны) : ")
origin_list = [int(i) for i in input().split()]
print("Список : " + str(origin_list))
max_element_index = origin_list.index(max(origin_list))
min_element_index = origin_list.index(min(origin_list))
origin_list[max_element_index], origin_list[min_element_index] = origin_list[min_element_index], origin_list[
    max_element_index]
print("Список после перестановки : " + str(origin_list))


