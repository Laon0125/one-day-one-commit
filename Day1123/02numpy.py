import numpy as np

print('라이브러리 처음')

# 216page 
a = [5,7,2]
# 리스트 항목 *3 15,21,6]
su = np.array(a)
gob = 0
total = 0

for k in su :
    dt = k*3
    print(dt, end = " ")
    gob += dt

print('gob 총합 = ', gob)