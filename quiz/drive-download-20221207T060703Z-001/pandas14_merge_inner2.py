'''
    pandas의 병합 ( db 의 조인기능)

    1. inner 병합 ( 조인 )
        - 두개의 df간에 일치하는 행만 반환

        가. 공통칼럼이 있는경우
            pd.merge(df1,df2, on='x1')
        나. 공통칼럼이 없는경우
            pd.merge(df1, df2, left_on=df1칼럼, right_on=df2칼럼)

    2. outer 병합 ( 조인 )
        - 두개의 df간에 모든 행 반환 (일치여부 상관 x)

        가. 공통컬럼이 있는경우
            pd.merge( df1, df2, on=공통컬럼, how='inner(기본)|right|left|outer)

            how='left' ===> 일치하지 않은 df1행 모두 반환
            how='right' ===> 일치하지 않은 df2행 모두 반환
            how='outer' ===> 일치하지 않은 df1,df2행 모두 반환

        나. 공통컬럼이 없는 경우
            pd.merge


    

'''

import numpy as np
import pandas as pd

df1 = pd.DataFrame({ 
    "x1" : ['A','B','C'],
    'x2' : [1,2,3]
    })

df2 = pd.DataFrame({ 
    "y1" : ['A','B','D'],
    'y2' : [10,20,30],
    'y3' : [9,8,6]
    })

print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  y1  y2  y3
0  A  10   9
1  B  20   8
2  D  30   6
'''

print('2. 공통칼럼이 없는경우')
new_df = pd.merge(df1, df2, left_on='x1', right_on='y1')
print(new_df)
'''
공통칼럼이 없는경우
  x1  x2 y1  y2  y3
0  A   1  A  10   9
1  B   2  B  20   8
'''




print('2. 공통칼럼이 없는경우')
new_df = pd.merge( df1, df2, left_on='x1', right_on = 'y1', how='right')
print(new_df)
new_df = pd.merge( df1, df2, left_on='x1', right_on = 'y1', how='left')
print(new_df)
new_df = pd.merge( df1, df2, left_on='x1', right_on = 'y1', how='outer')
print(new_df)
