import numpy as np

a = np.zeros(shape=(7,5)) #shapa 키워드는 생략 가능 #실수형
b = np.ones(shape=[3,4])
c = np.full((7,5),92)
print(c)
print()

d = np.full((7,5),23)
print(d)

x = np.full((7,5),0) #정수형
print(x)
y = np.full((7,5),1)
print(y)
z = np.eye(5)
print(z)

k = np.diag((7,9,5,1,3,8))
print(k)