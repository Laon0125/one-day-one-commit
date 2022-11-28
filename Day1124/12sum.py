
import numpy as np

a = [ 175, 177, 179, 181, 183 ]
my = np.array(a)
#1번째 총점 895 
#2번째 평균 179 
#3번째 분산 = 편차제곱/인원  np.var() 8    평균-개인점수=값*값 + ~~~ /인원수
#4번째 표준편차  np.std()  2.8284
#파이썬에서 합계구하는 변수 hap, total 

import math
my_mean = sum(my)/len(my) #895/5=179.0
my_value = sum( [(k-my_mean)**2  for k in my]  )  #40

my_var = my_value/len(my)
print('순수 총점 =', sum(my)) #895
print('순수 평균 =', sum(my)/len(my)) #179.0
print('순수 분산 =', my_var) #8.0
print('순수 표준편차 =', math.sqrt(my_var)) #2.8284
print('순수 표준편차 =', np.sqrt(my_var)) #2.8284
print('순수 표준편차 =', round(np.sqrt(my_var),2)) #2.8284

print()
print('넘피 총점 =', np.sum(my))
print('넘피 평균 =', np.mean(my))
print('넘피 분산 =', np.var(my))
print('넘피 표준편차 =', np.std(my))