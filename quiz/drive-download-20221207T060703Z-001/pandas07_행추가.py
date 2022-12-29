'''
     DataFrame에 행 추가 ==> df vs df

     1. 하나씩 추가
        df.append(df2)
         FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  new_df = df.append(df2, ignore_index=True)

     2. 한번에 여러개 ( 권장 )
        pd.concat([df,df2,.......], axis=0)
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"국어":[4,5,6,4,32],
                   "영어":[14,15,16,5,6],
                   "수학":[24,25,26,3,6]})
print(df)

df2 = pd.DataFrame({"국어":[99,95],
                   "영어":[94,95],
                   "수학":[94,95]})

new_df = df.append(df2, ignore_index=True)
print(new_df)


new_df = pd.concat([df,df2,df], axis=0, ignore_index=True)
print(new_df)
