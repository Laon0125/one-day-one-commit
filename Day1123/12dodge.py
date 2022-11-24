import numpy as np

a = np.zeros(shape=(7,5)) #shapa 키워드는 생략 가능 #실수형
b = np.ones(shape=[3,4])
c = np.full((7,5),92)
x = np.eye(5)
y = np.diag((7,9,5,1,3,8))
src = [ [74,1,2,3], [91,4,5,6,], [62,7,8,9] ]
print(src)
print()
srcarray = np.array(src)
srcdiag = np.diag(src)
print(srcarray)
print(srcdiag)