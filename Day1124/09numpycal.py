#09numpycal.py
#225~227페이지참고

import numpy as np

arr1 = np.array( [10,20,30,40])
arr2 = np.array( [1,2,3,4] )
# print(arr1);print(arr2)
print(arr1 + arr2)
print()
print(arr1 - arr2)
print()
print(arr1 * arr2)
print('-' * 70)
print()

print(arr2*2)
print(arr2**2)
print(pow(arr2,2))
print()

arr1 = np.array( [10,20,30,40])
arr2 = np.array( [1,5,6,5] )
print(arr1 / arr2)
print()
print()
print(arr1>20)