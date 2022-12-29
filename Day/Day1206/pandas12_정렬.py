'''
    정렬
    - 2가지 정류
        오름차순
        내림차순
    
    - 다중정렬 가능
    
    1. df.sort_values()
        -DB의 sql 에서 사용할 정렬



    2. df.sort_index()
'''

import numpy as np
import pandas as pd

import numpy as np
import pandas as pd
df = pd.DataFrame({"국어":[14,5,6,np.nan,32],
                   "영어":[14,15,16,5,np.nan],
                   "수학":[np.nan,25,26,3,6],
                   "과학":[4,5,6,34,5]},
                   index=list("BECAD"))
print(df)
print('1. 국어컬럼으로 오름차순 정렬')
df_new = df.sort_values(by=['국어'])
'''
1. 국어컬럼으로 오름차순 정렬
     국어    영어    수학  과학
E   5.0  15.0  25.0   5
C   6.0  16.0  26.0   6
B  14.0  14.0   NaN   4
D  32.0   NaN   6.0   5
A   NaN   5.0   3.0  34
'''
# df_new = df.sort_values(by=['국어'], ascending=False)
'''
     국어    영어    수학  과학
D  32.0   NaN   6.0   5
B  14.0  14.0   NaN   4
C   6.0  16.0  26.0   6
E   5.0  15.0  25.0   5
A   NaN   5.0   3.0  34
'''
df_new = df.sort_values(by=['국어'], ascending=False, na_position='first')
print(df_new)
'''
     국어    영어    수학  과학
A   NaN   5.0   3.0  34
D  32.0   NaN   6.0   5
B  14.0  14.0   NaN   4
C   6.0  16.0  26.0   6
E   5.0  15.0  25.0   5
'''
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
     'col2': [2, 1, 9, 8, 7, 4],
     'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
   })

print(df)
'''
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
'''
print('2. col1, col2로 다중정리')
new_df = df.sort_values(by=['col1','col2'])
'''
  col1  col2  col3 col4
1    A     1     1    B
0    A     2     0    a
2    B     9     9    c
5    C     4     3    F
4    D     7     2    e
3  NaN     8     4    D
'''
new_df = df.sort_values(by=['col1','col2'],ascending=False)
'''
2. col1, col2로 다중정리
  col1  col2  col3 col4
4    D     7     2    e
5    C     4     3    F
2    B     9     9    c
0    A     2     0    a
1    A     1     1    B
3  NaN     8     4    D
'''
print(new_df)

print('3. col4 컬럼으로 오름차순 정렬')
new_df = df.sort_values(by=['col4'])
new_df = df.sort_values(by='col4',key=lambda col: col.str.lower())
print(new_df)
'''
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
'''
print(ord('A'), chr(65))
print(ord('a'), chr(97))

def xxx(col):
    print(col, type(col))
    return col.str.lower()
new_df = df.sort_values(by='col4', key=xxx)