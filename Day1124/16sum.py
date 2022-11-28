import numpy as np


data= [  [1,2,3],[4,5,6],[7,8,9] ] #난수대신  3행x3열
b = np.array(data)

print('합계 =', np.sum(b)) #최종
print('총점 =', np.mean(b))
print('행합계 =', np.sum(b ,axis=1)) #행총점
print('열합계 =', np.sum(b ,axis=0)) #열총점
print('누적합계 =', np.cumsum(b)) #누적
