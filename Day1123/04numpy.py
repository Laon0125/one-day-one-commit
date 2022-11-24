import numpy as np

a = [5,7,2] # 리스트 1행 3열 = 0행*2열
data1 = np.array(a)
print(data1)
data2 = np.array(([5,7,2],[4,6,5],[7,6,5])) #어레이의 요소들을 하나씩 가저옴
print(data2)
data3 = np.array( [(5,7,2),(4,6,5),(2,3,4)])
print(data3)
