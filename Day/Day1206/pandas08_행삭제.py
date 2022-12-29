'''
    DataFrame에 컬럼 삭제

        1. 단일/다중 열 삭제
            df.drop(labels, axis= 0)
            df.drop()
           
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({
    '국어': [1,2,3,45,42],
    '영어': [4,5,6,75,76],
    '수학': [7,8,9,101,103],
    '한자': [4,5,6,75,76],
    '사회': [4,5,6,75,76],
    '가정': [4,5,6,75,76],
    '국사': [4,5,6,75,76]
    }, index=list("abcde")
)
print(df)

df.drop(['a','b'],inplace=True, axis = 0)
print(df)

df.drop(index=['d','e'],inplace=True)
print(df)