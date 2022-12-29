'''
    DataFrame에 행 추가 =>> df vs df

        1. 단일행 추가
            df.append('df2')

        2. 다중행 추가 (권장, 하나든 여러개든)
            df.concat([df,df2], axis = 0)
          
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({
    '국어': [1,2,3],
    '영어': [3,5,6],
    '수학': [7,8,9],
    '한자': [7,5,6]}
)
print(df)
df2 = pd.DataFrame({
    '국어': [1,2],
    '영어': [3,5],
    '수학': [7,8],
    '한자': [7,5]}
    )

new_df = df.append(df2, ignore_index=True)
print(new_df)

new_df = pd.concat([df,df2], axis = 0, ignore_index = True)
print(new_df)