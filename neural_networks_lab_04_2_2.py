import numpy as np


# С помощью нейронной сети на основе анализа набора характеристик, непонятно как влияющих на отнесение к классам,
# произвести классификацию транспортных средств по классам: Легковой автомобиль; Пассажирский транспорт; Грузовой
# транспорт. За основу взять следующие характеристики: 0) Большая снаряженная масса, 1) Большая мощность двигателя,
# 2) Большая пассажировместимость, 3) Большая грузоподъёмность.

def normalize(n, value):
    if n == 0:
        if value <= 0.5:
            return 0
        if 0.5 < value <= 1:
            return 0.25
        if 1 < value <= 2:
            return 0.50
        if 2 < value <= 5:
            return 0.75
        if value > 5:
            return 1
    if n == 1:
        if value <= 20:
            return 0
        if 20 < value <= 50:
            return 0.25
        if 50 <= value <= 100:
            return 0.50
        if 100 < value <= 200:
            return 0.75
        if value > 200:
            return 1
    if n == 2:
        if value <= 2:
            return 0
        if 2 < value <= 5:
            return 0.25
        if 5 < value <= 10:
            return 0.50
        if 10 < value <= 20:
            return 0.75
        if value > 20:
            return 1
    if n == 3:
        if value <= 1:
            return 0
        if 1 < value <= 2:
            return 0.25
        if 2 < value <= 3:
            return 0.50
        if 3 < value <= 4:
            return 0.75
        if value > 4:
            return 1


def normalizeX(value):
    tmp = [normalize(0, value[0]), normalize(1, value[1]), normalize(2, value[2]), normalize(3, value[3])]
    return tmp


def nonlin(value, deriv_value=False):
    if deriv_value:
        return value * (1 - value)
    return 1 / (1 + np.exp(-value))


X = np.array([normalizeX([0.645, 33, 4, 0.34]),
              normalizeX([2.880, 152, 14, 1.5]),
              normalizeX([1.110, 88, 5, 0.475]),
              normalizeX([10.400, 260, 3, 6]),
              normalizeX([2.880, 152, 3, 1.5]),
              normalizeX([9.895, 122, 30, 6.2]),
              normalizeX([3.695, 136, 3, 3]),
              normalizeX([2.170, 116, 5, 0.6]),
              normalizeX([27.895, 278, 150, 11])])
y = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0]])
np.random.seed(1)
syn0 = 2 * np.random.random((4, 5)) - 1
syn1 = 2 * np.random.random((5, 3)) - 1

for j in range(60000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l2_error = y - l2
    if (j % 10000) == 0:
        print('Error:', np.mean(np.abs(l2_error)))
    l2_delta = l2_error * nonlin(l2, deriv_value=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv_value=True)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

x = np.array([normalizeX([74, 1050, 1, 90]),
              normalizeX([13.6, 260, 10, 3]),
              normalizeX([0.3, 40, 3, 0.25]),
              normalizeX([0.2, 1, 4, 0.2]),
              normalizeX([0.02, 0.3, 1, 0.1]),
              normalizeX([18.4, 245, 168, 12])])
l0 = x
l1 = nonlin(np.dot(l0, syn0))
