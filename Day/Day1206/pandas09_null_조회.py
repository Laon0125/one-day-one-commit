'''
    null 조회 : None, np.nan, NA, NaN

    1. pandas 함수 이용
        pd.isna(df|Series|scalar)
        pd.isnull(df|Series)

        부정 (null 이 아닌가?)
        pd.notnull(df|Series)

    2. DataFrame 함수 이용
        df.isnull()
        df.["컬럼"].isnull()
        df.[['컬럼','컬럼']].isnull()


'''

import numpy as np
import pandas as pd

df = pd.DataFrame({
    '국어': [1,2,3,np.nan,32],
    '문어': [4,5,6,75,np.nan],
    '영어': [np.nan,np.nan,6,75,np.nan],
    '수학': [np.nan,np.nan,np.nan,np.nan,np.nan]}
)
print(df)
'''
    국어    문어    영어  수학
0   1.0   4.0   NaN NaN
1   2.0   5.0   NaN NaN
2   3.0   6.0   6.0 NaN
3   NaN  75.0  75.0 NaN
4  32.0   NaN   NaN NaN
'''
print(pd.isna(df))
'''
      국어     문어     영어    수학
0  False  False   True  True
1  False  False   True  True
2  False  False  False  True
3   True  False  False  True
4  False   True   True  True
'''
print(pd.isnull(df))
'''
      국어     문어     영어    수학
0  False  False   True  True
1  False  False   True  True
2  False  False  False  True
3   True  False  False  True
4  False   True   True  True
'''

print(pd.isna(df['국어']))
'''
0    False
1    False
2    False
3     True
4    False
Name: 국어, dtype: bool
'''
print(pd.isnull(df[['국어','영어']]))
'''
   국어     영어
0  False   True
1  False   True
2  False  False
3   True  False
4  False   True
'''

#긍정
m = '햄승연'
print(pd.isna(m))
print(pd.isnull(m))
print(pd.isna(np.nan))
print(pd.isnull(np.nan))

#부정
print(pd.notnull(df))
print(pd.notna(df))

