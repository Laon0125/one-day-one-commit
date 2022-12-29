'''

   import pandas as pd
   import numpy as np

   DataFrame 생성

   1. 중첩리스트
      df = pd.DataFrame(중첩리스트) ==> 컬럼레이블과 행레이블(인덱스)이 자동으로 0 1 2 형식으로 지정됨
      df = pd.DataFrame(중첩리스트, columns=[컬럼명,...])
      df = pd.DataFrame(중첩리스트, columns=[컬럼명,...], index=[인덱스명,...])
'''
import numpy as np
import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(arr)
print(df, type(df))

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["c1","c2","c3"])
print(df, type(df))

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["c1","c2","c3"], index=['A','B','C'])
print(df, type(df))