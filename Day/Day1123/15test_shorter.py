import numpy as np

my = [ 175, 177, 179, 181, 183]
# 넘피 이용하지 않고 수작업으로 처리
# 첫번쨰 총점, 평균
hap = 0
avg = 0
for i in my :
    hap += i 

avg = hap / 5
print('일반총점 = ', hap)
print('일반평균 = ', avg)

import math
my_mean = sum(my)/len(my)
my_var = sum([(my_mean-k)**2 for k in my])/len(my)

print('분산')
