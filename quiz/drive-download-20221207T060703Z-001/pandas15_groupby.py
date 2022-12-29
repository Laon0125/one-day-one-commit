'''

@ 그룹핑
    특정 컬럼을 묶을때 (그룹핑)
    예) 성별,힉년, 부서별 등등
    df.groupby(by='컬럼명')[컬럼].그룹함수

'''

import numpy as np
import pandas as pd

df = pd.DataFrame({"사원번호":['A1','A2','A3','A4','A5'],
                    "월급":[100,200,150,250,120],
                    "성별":['M',"F","F","M","M"],
                    "부서번호":[10,20,10,20,30]})
print(df)

# 1. 부서별 sal 최대값  
new_df = df.groupby(by="부서번호")['월급'].max()
new_df = df.groupby(by="부서번호")['월급'].min()
new_df = df.groupby(by="부서번호")['월급'].sum()
new_df = df.groupby(by="부서번호")['월급'].mean()
new_df = df.groupby(by="부서번호")['월급'].count()
print(new_df)
print(new_df.to_frame()) # Series --> dataframe 으로 변경

print(df)

# 2. 부서별 성별 월급
new_df = df.groupby(by=["부서번호",'성별'])['월급'].max()
print(new_df)