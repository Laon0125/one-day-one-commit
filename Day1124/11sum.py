
import numpy as np

#227페이지참고 
arr3 = np.arange(5) #0부터~4까지만 5개발생
print(arr3)
print('총점 =', np.sum(arr3))
print('평균 =', np.average(arr3))
print('평균 =', np.mean(arr3))
print('분산 =', np.var(arr3))
print('표준편차 =', np.std(arr3))
print()

a = [ 175, 177, 179, 181, 183 ]
total,avg = 0,0
for k in a:
    total = total + k

avg = total/len(a) 
print('일반총점 =', total) #895
print('일반평균 =', avg)   #179