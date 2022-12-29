import numpy as np


# a = np.random.rand(3,5) #3행*5열 
# print(a)
# print()

np.random.seed(20)
b = np.random.rand(15).reshape(3,5)  #3행*5열 
print(b)
print()

print('합계 =', np.sum(b))
print('총점 =', np.mean(b))
print('행합계 =', np.sum(b ,axis=1)) #행총점
print('열합계 =', np.sum(b ,axis=0)) #열총점
print('누적합계 =', np.cumsum(b)) #누적 
