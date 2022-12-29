import numpy as np

#218page참고
x = np.arange(12).reshape(4,3) #4행*3열
print(x)
print('-' * 70)
print()

# 에러발생y = np.arange(12).reshape(6,3) #6행*3열  ===>데이터는부족, 공간 18개
# print(y)
# print()

# 에러발생z = np.arange(12).reshape(3,2) #3행*2열  ===>데이터는넘쳐요, 공간 부족
# print(z)
# print()