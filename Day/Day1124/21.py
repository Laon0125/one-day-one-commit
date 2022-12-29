import numpy as np

a = np.array( [ [2,4], [5,7] ])
b = np.array( [ [6,1], [3,9] ])
print(a)
print()

# retA = a.dot(a)
retB = np.dot(a,b)
print (retB)


'''
[1,2]  [1,2]
[3,4]  [3,4]

1 * 1 + 2 * 3 = 7
1 * 2 + 2 * 4 = 10
3 * 1 = 4 * 3 = 15
3 * 2 + 4 * 4 = 22

'''