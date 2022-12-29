import numpy as np


data = [ [1,2,3],[4,5,6],[7,8,9] ]
b = np.array(data)

print('합계 = ', np.sum(b))
print('총점= ', np.mean(b))
print('열합계 = ', np.sum(b,axis=0))       #열총점
print('행합계 = ', np.sum(b,axis=1))       #행총점
print('누적합계 = ', np.cumsum(b))

print('최대값 = ', np.max(b))
print('최소값 = ', np.min(b))
print('충앙값 = ', np.median(b))            #짝수개의 중앙값은 양 옆의 숫자의 평균임
