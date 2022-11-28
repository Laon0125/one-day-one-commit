a = [5,7,2]

#print(a+3)  #에러
#print(a*3)  #반복으로 인식 에러없음
#print()
#에러 print(a*0.3)  

import numpy as np
b = np.array(a)
print(b+3)   #연산
print()
print(b+0.3)  #연산
