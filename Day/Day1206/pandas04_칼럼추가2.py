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
    '영어': [4,5,6,75,76],
    '수학': [7,8,9,101,103]}
)
print(df)
'''
   국어  영어   수학
0   1   4    7
1   2   5    8
2   3   6    9
3  45  75  101
4  42  76  103
'''

# 1. 과학 추가
df = df.assign(과학=[4,5,6,4,32])
print(df)
'''
   국어  영어   수학  과학
0   1   4    7   4
1   2   5    8   5
2   3   6    9   6
3  45  75  101   4
4  42  76  103  32
'''
# 총합컬럼 추가
# def total_sum(x):
#     return  df['국어']+df['영어']+df['수학']+df['과학']

# df = df.assign(총합=total_sum) 
# print(df)

df = df.assign(총합=lambda df:+df['영어']+df['수학']+df['과학'])
print(df)


# 평균칼럼 추가
# def avg(x):
#     return df['총합']/4
# df = df.assign(평균=avg)

df = df.assign(평균=lambda df:df['총합']/4)
print(df)

# 합격여부 출력 (평균값이 10이상이면 합격)

df = df.assign(합격=lambda dv: ['합격' if avg >40 else '불합격' for avg in df['평균']])
print(df)