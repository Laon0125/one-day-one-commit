'''
     null 조회 :  None, np.nan, NA, NaN

     1. Pandas 함수 이용
          null 이냐?
          pd.isna(df|Series|scalar)
          pd.isnull(df|Series)

         부정 (null이 아니냐?)
          pd.notnull(df|Series|scalar)
         ~pd.isna(df|Series|scalar)

     2. DataFrame 함수 이용
         df.isnull()
         df["컬럼"].isnull()
         df[["컬럼","컬럼"]].isnull()

'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"국어":[4,5,6,np.nan,32],
                   "영어":[14,15,16,5,np.nan],
                   "수학":[np.nan,25,26,3,6],
                   "과학":[np.nan,np.nan,np.nan,np.nan,np.nan]})
print(df)

#  null 찾기
print(pd.isna(df))
print(pd.isnull(df))

print(pd.isna(df["국어"]))
print(pd.isna(df[["국어","영어"]]))
print(pd.isnull(df["국어"]))
print(pd.isnull(df[["국어","영어"]]))

m = "홍길동"
print(pd.isna(m)) # False
print(pd.isnull(m)) # False
print(pd.isna(np.nan)) # True
print(pd.isnull(np.nan)) # True

# 부정
print(pd.notnull(df))
print(~pd.isnull(df))