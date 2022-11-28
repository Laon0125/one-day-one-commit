import numpy as np

#224page 넘피의 난수 
a = np.random.rand(3,5)    #rand()  3행 * 5열  양수실수 0.00000 ~ 0.9999
b = np.random.randn(3,5)   #randn()  3행 * 5열 음수양수 실수 -1.453 ~ +1.9823 
c = np.random.randint(3,5) #randint() 3~5사이의 숫자 하나만 발생
print('np.rando.randint(3,5)')
print(c)
print()

import random
print('randint(1,45)')
print(random.randint(1,45)) #로또숫자발생1~45
print()