import numpy as np
import random
import hello

#  a) Вычислите логарифм по основанию 2 от 15.

print(np.log2(15))

#  b) Сгенерируйте четыре раза одно и то же число, равномерно распределенное на интервале (0; 1).

random.seed(1)
print("Первое число :", random.uniform(0, 1))
random.seed(1)
print("Второе число :", random.uniform(0, 1))
random.seed(1)
print("Третье число :", random.uniform(0, 1))
random.seed(1)
print("Четвёртое число :", random.uniform(0, 1))

#  c) Определите список имен, определенных в данный момент.

print(dir())

#  d) Создайте и выполните свой модуль на языке Python.

print("Введите своё имя : ")
name = input()
hello.say_hello(name)
