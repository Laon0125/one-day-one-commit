import numpy as np


data= [  [5,2,3],[4,34,16],[17,28,19] ] #난수대신  3행x3열
b = np.array(data)

print('합계 =', np.sum(b)) #최종
print('총점 =', np.mean(b))
print('행합계 =', np.sum(b ,axis=1)) #행총점
print('열합계 =', np.sum(b ,axis=0)) #열총점
print('누적합계 =', np.cumsum(b)) #누적
print('최대값 =', np.max(b))
print('최소값 =', np.min(b))
print('중앙값 =', np.median(b)) #16
print('평균값 =', np.mean(b))   #14.222

#2 3 4 5  16  17 19 28 34
data= [  [5,2,3],[4,34,16],[17,28,19] ] #난수대신  3행x3열