'''
    null 삭제

'''
import pandas as pd
import numpy as np

df = pd.DataFrame({"국어":[4,5,6,np.nan,np.nan],
                   "영어":[14,15,16,5,np.nan],
                   "체육":[np.nan,np.nan,np.nan,np.nan,np.nan],
                   "수학":[np.nan,25,26,3,np.nan],
                   "과학":[np.nan,np.nan,np.nan,np.nan,np.nan]})



print(df)

new_df = df.dropna(axis=0, how='any')
print(new_df)

new_df = df.dropna(axis=1, how='any')
print(new_df)


print(df)

new_df = df.dropna(axis=0, how='all')
print(new_df)

new_df = df.dropna(axis=1, how='all')
print(new_df)

