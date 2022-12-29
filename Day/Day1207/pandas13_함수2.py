'''
    DataFrame Fuctions

    1. 기술통계관련 함수
        합계/누적합계           df.sum(axis)
        곱/누적곱              df.comsum(axis)
        분산 표준편차           df.var() / df.std(axis)
        4분위 수              df.quantile( 백분율 )           df.var() / df.std(axis)
        행갯수                 df.count(axis = 0)

         전채 통계정보  df.subscribe

    2. 축을 바꾸고 싶다면 axis=1



'''


import numpy as np
import pandas as pd

df = pd.DataFrame({ 'c1' : [4,5,6, np.nan, 1],
                    'c2' : [14,15,16,55,4],
                    'c3' : [24,25,26,76,3]})
df.info()
print(df)
'''
    c1  c2  c3
0  4.0  14  24
1  5.0  15  25
2  6.0  16  26
3  NaN  55  76
4  1.0   4   3
'''

print('1. df 컬럼별 (행축) 최대 최소값')
x = df.max(axis=0)
y = df.min(axis=0)
print(x,y)

x = df.cummax(axis=0)
x = df.cummin(axis=0)

x = df.idxmax(axis=0)
y = df.idxmin(axis=0)

x = df.prod(axis=0)
y = df.cumprod(axis=0)

# 분산 표준편차

x = df.var(axis=0)
x = df.std(axis=0)

# 행 갯수

x = df.count(axis=0)
print(x)

#  컬럼별 사분위수 ( percentile ) 데이터가 분포되어있을ㄸ ㅒ얼마나 분포되어있는지 알수있음 4분율로 

# 사분위수

df = pd.DataFrame({"price":[10,20,30,40,1,2,3,4,5]})

print(df, sorted(df['price']))

x = df.quantile([0.25,0.5,0.75])
print(x)

x = df.quantile(0.75) - df.quantile(0.25)
print(x)

#

