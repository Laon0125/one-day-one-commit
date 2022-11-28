import numpy as np

def myCal (x,y) :
    hap = 10*x+y
    return hap

total = myCal(5,2)
print('결과 = ', total)
print('결과 = ', myCal(5,2))

dt = np.fromfunction(myCal, (5,2), dtype=int) #어떻게 작동하는지 이해가 안됌... 주의 요망
print(dt)