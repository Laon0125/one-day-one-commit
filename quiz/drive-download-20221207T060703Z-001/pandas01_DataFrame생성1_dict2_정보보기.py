'''

   import pandas as pd
   import numpy as np

   DataFrame 정보 얻기

   1. 컬럼 정보
       df.columns  속성
       df.keys()   함수

   2. 인덱스 정보
       df.index

   3. 내용
     df.values
     df.to_numpy() - 권장함
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"c1":[4,5,6],
                   "c2":[14,15,16],
                   "c3":[24,25,26]})
# 1. 컬럼 정보
print(df.columns, list(df.columns)) # Index(['c1', 'c2', 'c3'], dtype='object') ['c1', 'c2', 'c3']
print(df.keys(), list(df.keys())) # Index(['c1', 'c2', 'c3'], dtype='object') ['c1', 'c2', 'c3']

# 2. 인덱스 정보 ( 행라벨 정보 )
print(df.index) # RangeIndex(start=0, stop=3, step=1)

# 3. 내용
print(df.values)
print(df.to_numpy())