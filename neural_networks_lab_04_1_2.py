import numpy as np


def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([[0], [1], [1], [0]])

np.random.seed(1)
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for iter in range(60000):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l2_error = y - l2
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)
    if iter == 0:
        print("l2 после первой итерации : ", "\n", l2)
        print("l2_error после первой итерации : ", "\n", l2_error)
    if iter == 59999:
        print("l2 после последней итерации : ", "\n", l2)
        print("l2_error после последней итерации : ", "\n", l2_error)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

'''
l2 после первой итерации :  
 [[0.47372957][0.48895696][0.54384086][0.54470837]]
l2_error после первой итерации :  
 [[-0.47372957][ 0.51104304][ 0.45615914][-0.54470837]]
 
l2 после последней итерации :  
 [[0.00260572][0.99672209][0.99701711][0.00386759]]
l2_error после последней итерации :  
 [[-0.00260572][ 0.00327791][ 0.00298289][-0.00386759]]
'''