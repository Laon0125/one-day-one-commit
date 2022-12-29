'''

   import pandas as pd
   import numpy as np

   DataFrame 컬럼(컬럼 레이블) 및 인덱스(행 레이블) 변경

   1. 컬럼 변경
       df.columns=[컬럼명,...]
       
   2. 인덱스 정보 1 ( df 생성후에 나중에 변경 )
       df.index=[인덱스명,...]

   3. 인덱스 정보 2 ( df 생성하면서 변경 )

      df = pd.DataFrame({key:값, key:값}, index=[인덱스명,...])
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"c1":[4,5,6],
                   "c2":[14,15,16],
                   "c3":[24,25,26]})
# 1. 원본
print(df)

# 2. 컬럼명 변경
df.columns=["col1","col2","col3"]
print(df)

# 3. 인덱스 ( 행 레이블) 변경 ==> 기본은 0 1 2 ... 지정됨.
df.index=[10,20,30]
df.index=["A","B","C"]
print(df)

# 3. 인덱스 ( 행 레이블) 변경
df = pd.DataFrame({"c1":[4,5,6],
                   "c2":[14,15,16],
                   "c3":[24,25,26]},
                    index=["A1","B1","C1"])
print(df)