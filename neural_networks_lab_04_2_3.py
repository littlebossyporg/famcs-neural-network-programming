import numpy as np


def nonlin(value, deriv_value=False):
    if deriv_value:
        return value * (1 - value)
    return 1 / (1 + np.exp(-value))


X = np.array([[111100, 1000010, 1000000, 1000000, 1000000, 1000000, 1000010, 111100],
              [1111110, 1000000, 1000000, 1111100, 1000000, 1000000, 1000000, 1111110],
              [11000, 100100, 100100, 100100, 100100, 100100, 1111110, 1000010]])
y = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])
X = X
y = y
np.random.seed(1)
syn0 = 2 * np.random.random((8, 10)) - 1
syn1 = 2 * np.random.random((10, 3)) - 1
print(syn0)
print(syn1)

for j in range(60000):
    l0 = X
    l11 = np.dot(l0, syn0)
    l1 = nonlin(l11)
    l22 = np.dot(l1, syn1)
    l2 = nonlin(l22)
    l2_error = y - l2
    if (j % 5000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
    l2_delta = l2_error * nonlin(l2, deriv_value=True)
    l1_error = np.dot(l2_delta, syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv_value=True)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
X = np.array([[110100, 1000010, 1000000, 1000000, 1000000, 1000000, 1000010, 111100],
              [1111110, 1000000, 1000000, 1101100, 1000000, 1000000, 1000000, 1111110]])
y = np.array([[1, 0, 0]])
X = X
y = y
l0 = X
l11 = np.dot(l0, syn0)
l1 = nonlin(l11)
l22 = np.dot(l1, syn1)
l2 = nonlin(l22)
print('знач. прогноза: ', l2)
