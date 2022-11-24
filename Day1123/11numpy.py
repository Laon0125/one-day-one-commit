import numpy as np

a = np.zeros(shape=(7,5)) #shapa 키워드는 생략 가능 #실수형
b = np.ones(shape=[3,4])
c = np.full((7,5),92)
d = np.full((7,5),23)
x = np.full((7,5),0) #정수형
y = np.full((7,5),1)
z = np.eye(5)

k = np.diag((7,9,5,1,3,8))
print(k)
'''
[[7 0 0 0 0 0]
 [0 9 0 0 0 0]
 [0 0 5 0 0 0]
 [0 0 0 1 0 0]
 [0 0 0 0 3 0]
 [0 0 0 0 0 8]]
 '''