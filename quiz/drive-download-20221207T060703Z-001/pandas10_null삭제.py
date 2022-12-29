'''
     null 삭제

     1. 행삭제
        df.dropna( axis=0, how="any|all")

     def dropna(self,
           axis: str | int = 0,
           how: str | _NoDefault = no_default, # 하나라도 nan이면 삭제 또는 모두 nan 삭제
           thresh: int | _NoDefault = no_default,
           subset: Hashable | Sequence[Hashable] | None = None,
           inplace: bool = False) -> DataFrame | Non

     2. 열삭제
        df.dropna( axis=1, how="any|all")

'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"국어":[4,5,6,np.nan,32],
                   "영어":[14,15,16,5,np.nan],
                   "수학":[np.nan,25,26,3,6],
                   "과학":[4,5,6,34,5]})
print(df)
'''
     국어    영어    수학  과학
0   4.0  14.0   NaN   4
1   5.0  15.0  25.0   5
2   6.0  16.0  26.0   6
3   NaN   5.0   3.0  34
4  32.0   NaN   6.0   5
'''
print("1. 하나라도 nan이면 행 삭제")
new_df = df.dropna(axis=0, how="any")
print(new_df)

print("2. 하나라도 nan이면 열 삭제")
new_df = df.dropna(axis=1, how="any")
print(new_df)

df = pd.DataFrame({"국어":[4,5,6,np.nan,np.nan],
                   "영어":[14,15,16,5,np.nan],
                   "수학":[np.nan,25,26,3,np.nan],
                   "과학":[4,5,6,34,np.nan],
                   "체육":[np.nan,np.nan,np.nan,np.nan,np.nan]})
print(df)
print("3. 모두 nan이면 행 삭제")
new_df = df.dropna(axis=0, how="all")
print(new_df)

print("4. 모두 nan이면 열 삭제")
new_df = df.dropna(axis=1, how="all")
print(new_df)