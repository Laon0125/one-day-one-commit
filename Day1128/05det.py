import numpy as np
a = np.array([[1, 2], [3, 4]]) 
#a = np.array([[1a, 2b], [3c, 4d]]) 
print("결과 =", np.linalg.det(a)) #-2.0   a*d-b*c= 1*4-2*3
print()

a = np.array([[1, 2], [3, 4]]) 
#a = np.array([[-d, +b], [+c, -a]]) 
print("결과 =", np.linalg.inv(a))
print() 
'''
[[-2.   1. ] 
 [ 1.5 -0.5]]
'''