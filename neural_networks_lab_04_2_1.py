import numpy as np


# Построить прогноз курса доллара США на основе курсов за 4 предшествующих дня на основе имеющихся у нас значений
# курса за 13 дней начиная с 01.01.2019
def nonlin(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


X = np.array([[2.1598, 2.1598, 2.1701, 2.1788],
              [2.1598, 2.1701, 2.1788, 2.1727],
              [2.1701, 2.1788, 2.1727, 2.1727],
              [2.1788, 2.1727, 2.1727, 2.1727],
              [2.1727, 2.1727, 2.1727, 2.1727],
              [2.1727, 2.1727, 2.1727, 2.159],
              [2.1727, 2.1727, 2.159, 2.1569],
              [2.1727, 2.159, 2.1569, 2.1532],
              [2.159, 2.1569, 2.1532, 2.1503]])
normX = np.linalg.norm(X)
X = X / normX
y = np.array([[2.1727, 2.1727, 2.1727, 2.1727, 2.159, 2.1569, 2.1532, 2.1503, 2.1503]]).T
y = y / normX
np.random.seed(1)
syn0 = 2 * np.random.random((4, 1)) - 1

for counter in range(10000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l1_error = y - l1
    l1_delta = l1_error * nonlin(l1, True)  # !!!
    if counter % 1000 == 0:
        print('Error:', np.mean(np.abs(l1_error)))
    syn0 += np.dot(l0.T, l1_delta)
x = [2.1569, 2.1532, 2.1503, 2.1503]
x = x / normX
l0 = x
l1 = nonlin(np.dot(l0, syn0)) * normX
print("Forecast for the US dollar : ", l1)
