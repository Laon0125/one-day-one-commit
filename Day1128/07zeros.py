import numpy as np

a = np.zeros((7,5))
b = np.zeros([7,5])
c = np.array((0,0,7,5,2,9,0,0))
print(c)
print(np.trim_zeros(c))
print(np.trim_zeros(c,trim='f'))
print(np.trim_zeros(c,trim='b'))
print(np.zeros(12))