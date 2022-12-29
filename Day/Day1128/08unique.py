import numpy as np


c = np.array((9,1,9,9,5,3,6,8,29,29,9,29))
print(c)

print()
print(np.unique(c)) #낮은순으로 소트, 중복제거

b = np.array([ [8,7,0], [5,0,0], [2,3,0],[2,3,0]])
print(np.unique(b))
print(np.unique(b,axis=0))
print(np.unique(b,axis=1))
