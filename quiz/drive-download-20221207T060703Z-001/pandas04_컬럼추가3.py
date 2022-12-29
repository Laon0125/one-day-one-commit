'''
     DataFrame에 컬럼 추가

     1.
       df["새로운컬럼"]=값(리스트)

     2. df.assign(컬럼명=리스트, 컬럼명=리스트,...)

     3. df와 df2 연결
        pd.concat([df, df2], axis=1)
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"국어":[4,5,6,4,32],
                   "영어":[14,15,16,5,6]})
df2 = pd.DataFrame({"수학":[24,25,26,3,6]})

new_df = pd.concat([df, df2], axis=1)
print(new_df)