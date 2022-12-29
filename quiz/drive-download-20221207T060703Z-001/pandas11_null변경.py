'''
     null 값 변경

     1. 임의의 값으로 변경 ( 대표적으로 평균값, 중앙값 )

          df.fillna(임의의 값)
          df.fillna({컬럼명:값, 컬럼명:값})

          def fillna(self,
           value: Hashable | Mapping(딕셔너리, Map계열) | Series | DataFrame | None = None,
           method: Literal["backfill", "bfill", "ffill", "pad"] | None = None,
           axis: str | int | None = None,
           inplace: bool = False,
           limit: int | None = None,
           downcast: dict | None = None) -> NDFrameT | None

     2. null 앞(forward)에 있는 값, 뒤(backward)에 있는 값으로 변경

          df.fillna(method="ffill") ==> null 앞(forward)에 있는 값으로 치환
          df.fillna(method="bfill") ==> null 뒤(backward)에 있는 값으로 치환

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

print("1. 모든 null값을 임의값으로 변경")
new_df = df.fillna(0)
print(new_df)

print("2. 컬럼단위로 null값을 임의값으로 변경")
new_df = df.fillna({"국어":0,"영어":-10,"수학":-20})
print(new_df)

df = pd.DataFrame({"국어":[4,5,6,np.nan,32],
                   "영어":[14,np.nan,16,5,10],
                   "수학":[52,np.nan,25,26,3],
                   "과학":[4,5,6,34,5]})
print(df)
'''
     국어    영어    수학  과학
0   4.0  14.0  52.0   4
1   5.0   NaN   NaN   5
2   6.0  16.0  25.0   6
3   NaN   5.0  26.0  34
4  32.0  10.0   3.0   5
'''
print("3. null 앞(forward)에 있는 값으로 치환")
new_df = df.fillna(method="ffill")
print(new_df)

print("4. null 뒤(backward)에 있는 값으로 치환")
new_df = df.fillna(method="bfill")
print(new_df)