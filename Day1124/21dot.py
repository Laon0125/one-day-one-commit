import numpy as np

#229페이지  행렬연산  표 11-2참고하세요
a = np.array( [ [1,2], [3,4] ] )
print()

#retA = a.dot(a)
retB = np.dot(a,a)
print(retB)
print('-' * 70)

# b = np.array( [ [1,2], [3,4] ] )
# retC = np.linalg.det(b)
# print(retC)