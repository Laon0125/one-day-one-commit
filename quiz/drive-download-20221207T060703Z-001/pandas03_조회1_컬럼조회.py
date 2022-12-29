'''
   DataFrame 조회

   1. 컬럼 조회 ( projection )

       df.컬럼명  ==> Series 반환
       df['컬럼명'] ==> Series 반환

       df[ ['컬럼명','컬럼명',...  ] ] ==> DataFrame 반환

'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"c1":[4,5,6],
                   "c2":[14,15,16],
                   "c3":[24,25,26]})

print(df.c1, type(df.c1))
print(df['c3'], type(df['c3']))
print(df[['c3','c1']], type(df[['c3','c1']]))

# 동일 컬럼 여러번 지정 가능하다.
print(df[['c3','c1','c1','c1']])