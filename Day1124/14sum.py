import numpy as np


# a = np.random.rand(3,5) #3행*5열대신  3에서~5사이숫자
# print(a)
# print()

np.random.seed(20)  #같은데이터 난수발생
b = np.random.rand(15).reshape(3,5)  #3행*5열 구성일때  가로합계, 세로합계, 누적합계
print(b)
print('행합계 =', np.sum(b ,axis=1)) #행총점
print('열합계 =', np.sum(b ,axis=0)) #열총점
print()
print('누적합계 =', np.cumsum(b)) #누적
print('합계 =', np.sum(b)) #최종값
print()
