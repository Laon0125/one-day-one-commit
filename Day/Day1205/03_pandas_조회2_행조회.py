'''
    1. 컬럼 조회 
        df.컬럼명 ==> 시리즈 반환
        df['컬럼명'] ==> 시리즈 반환
        
        df[ [ '컬럼명' , ' 컬럼명' ,...]] ==> dataFrame 반환

    2. 행 조회
        가. 행 라벨 이용
            df.loc[] ==> 인덱싱 색인
            df.loc[[헹라벨1,행라벨2]] ==> 인덱싱 색인
            df.loc[행라벨1:행라벨2] ==> 인덱싱 색인
            
        

        나. 행 위치 이용
            df.iloc[] ==> 인덱싱
            df.iloc[[행위치, 행위치]] ==> fancy
            df.iloc[start행워치:stop행위치] ==> slice


'''

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'c1': [1,2,3,45,42],
    'c2': [4,5,6,75,76],
    'c3': [7,8,9,101,103]},
    index= list("ABCDE")
)

print(df)
'''
   c1  c2   c3
A   1   4    7
B   2   5    8
C   3   6    9
D  45  75  101
E  42  76  103
'''

print(df.loc['B'], type(df.loc['B']))
print(df.loc[["B","C"]], type(df.loc[["B","C"]]))

print(df.loc['B':'E'], type(df.loc["B":"E"]))

print(df.loc[[True,True,False,False,True]])


# 2. 행 위치로 조회

print(df.iloc[0])
'''
c1    1
c2    4
c3    7
'''
print(df.iloc[-1])
'''
c1     42
c2     76
c3    103
'''

print(df.iloc[[0,2,-1]])
'''
   c1  c2   c3
A   1   4    7
C   3   6    9
E  42  76  103
'''

print("-----------------------------")

print(df.iloc[1:4])
'''
 c1  c2   c3
B   2   5    8
C   3   6    9
D  45  75  101
'''
print(df.iloc[::4])
'''
c1  c2   c3
A   1   4    7
E  42  76  103
'''

print(df.iloc[[True,False,False,False,False]])
'''
 c1  c2  c3
A   1   4   7
'''