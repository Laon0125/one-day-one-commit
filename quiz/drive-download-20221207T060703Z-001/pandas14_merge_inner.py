'''
    pandas의 병합 ( db 의 조인기능)

    1. inner 병합 ( 조인 )
        - 두개의 df간에 일치하는 행만 반환

        가. 공통칼럼이 있는경우

    2. outer 병합 ( 조인 )
        - 두개의 df간에 모든 행 반환 (일치여부 상관 x)

    

'''

import numpy as np
import pandas as pd

df1 = pd.DataFrame({ 
    "x1" : ['A','B','C'],
    'x2' : [1,2,3]
    })

df2 = pd.DataFrame({ 
    "x1" : ['A','B','D'],
    'x2' : [10,20,30],
    'x3' : [9,8,6]
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
  x1  x2  x3
0  A  10   9
1  B  20   8
2  D  30   6
'''

print('1. 공통컬럼이 있는경우')
new_df = pd.merge(df1,df2, on='x1')
'''
  x1  x2_x  x2_y  x3
0  A     1    10   9
1  B     2    20   8
'''

new_df = pd.merge(df1,df2[['x1','x3']], on='x1')
'''
1. 공통컬럼이 있는경우
  x1  x2  x3
0  A   1   9
1  B   2   8
'''
print(new_df)
