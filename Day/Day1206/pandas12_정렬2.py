'''
    정렬
    - 2가지 정류
        오름차순
        내림차순
    
    - 다중정렬 가능
    
    1. df.sort_values()
        -DB의 sql 에서 사용할 정렬



    2. df.sort_index()

        가. 헹의 인덱스 (레이블 ) 정렬
        
        나. 열의 인덱스 (레이블 ) 정렬

'''

import numpy as np
import pandas as pd

df = pd.DataFrame({ 
    'Korean' : [14,5,6,np.nan,32],
    'English' : [14,15,16,4,np.nan],
    'Math' : [np.nan,2,3,6,3], 
    'Science' : [2,12,5,8,34]},
    index = list('BECAD'))
# 1.  열 인덱스
new_df = df.sort_index(axis=0)
print(new_df)
'''
 Korean  English  math  science
A     NaN      4.0   6.0        8
B    14.0     14.0   NaN        2
C     6.0     16.0   3.0        5
D    32.0      NaN   3.0       34
E     5.0     15.0   2.0       12
'''
new_df = df.sort_index(axis=0,ascending=False)
print(new_df)
'''
   Korean  English  math  science
E     5.0     15.0   2.0       12
D    32.0      NaN   3.0       34
C     6.0     16.0   3.0        5
B    14.0     14.0   NaN        2
A     NaN      4.0   6.0        8
'''

# 2. 행 인덱스

new_df = df.sort_index(axis=1,ascending=False)
print(new_df)