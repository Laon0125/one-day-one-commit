import numpy as np

# 문제 0~1사이 숫자 발생 4행 5열

data = np.arange(20).reshape(4,5) # 굉장히 굳! array 쓰는것보다 휠씬 편함
path = './Day1128/data/encore.txt'
print(data)
np.savetxt(path, data, fmt='%2d')
print()
print(path, 'saving...')
print(path, ' file saved')
print(path, ' file loading')

import time
time.sleep(2)
ret= np.loadtxt(path)
ret= np.loadtxt(path,dtype='int')
print(ret)