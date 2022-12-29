'''
    DataFrame에 컬럼 추가

    1. df['새로운 컬럼']= 값(리스트)

    2. df.assign(컬럼명= 리스트, 컬럼명 = 리스트,...)

    3. df와 df 2 연결
        pd.concat()
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({
    '국어': [1,2,3,45,42],
    '영어': [4,5,6,75,76]}
)
df2 = pd.DataFrame({
    '수학': [7,8,9,101,103]}
)

new_df = pd.concat([df,df2], axis=1)
print(new_df)