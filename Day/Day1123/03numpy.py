import numpy as np

a = [5,7,2] # 리스트 1행 3열 = 0행*2열
data1 = np.array(a)
print(data1)
data2 = np.array([5,7,2]) #어레이의 요소들을 하나씩 가저옴
print(data2)
data3 = np.array( (5,7,2))
print(data3)

# error 이건 안돼는게 5,7,2를 각각 하나의 어래이로 봄
# data4 = np.array( 5,7,2) 
# print(data2)