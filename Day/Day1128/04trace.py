import numpy as np

# 4행  4열 0~15정수 숫자 발생
# np.array(), np.arrange(16)
a = np.arange(16).reshape(4,4)
# a = np.array(16).reshape(6,4) 에러
print(a)
print(np.trace(a)) # 가장 긴 대각선의 합... 30


b = np.arange(27).reshape(3,3,3)
print(b)
print(np.trace(b))