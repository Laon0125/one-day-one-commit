'''
   DataFrame 조회

   1. 컬럼 조회 ( projection )

       df.컬럼명  ==> Series 반환
       df['컬럼명'] ==> Series 반환

       df[ ['컬럼명','컬럼명',...  ] ] ==> DataFrame 반환


   2. 행 조회 ( selection )

     가. 행 라벨 이용
        df.loc[행라벨] ==> 인덱싱 색인
        df.loc[[행라벨,행라벨,..]] ==> fancy 색인
        df.loc[행라벨1:행라벨2] ==> 슬라이싱 색인, 행라벨2 포함됨
        df.loc[[True,...]] ==> 불린 색인
        

     나. 행 위치 이용 ( 순방향/역방향 모두 가능 )
        df.iloc[행위치] ==> 인덱싱 색인
        df.iloc[[행위치,행위치,..]] ==> fancy 색인
        df.iloc[start행위치:stop행위치] ==> 슬라이싱 색인, stop행위치 전까지
        df.iloc[[True,...]] ==> 불린 색인
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"c1":[4,5,6,4,32],
                   "c2":[14,15,16,5,6],
                   "c3":[24,25,26,3,6]},
                   index=list("ABCDE"))
print(df)
'''
     c1  c2  c3
0 A   4  14  24
1 B   5  15  25
2 C   6  16  26
3 D   4   5   3
4 E  32   6   6
'''
# 1. 행레이블로 조회
print(df.loc['B'], type(df.loc['B']))
print(df.loc[['B','C']], type(df.loc[['B','C']]))
print(df.loc['B':'E'], type(df.loc['B':'E']))
print(df.loc[[True,False,False,False,False]])

'''
     c1  c2  c3
0 A   4  14  24
1 B   5  15  25
2 C   6  16  26
3 D   4   5   3
4 E  32   6   6
'''
# 2. 행 위치로 조회
print(df.iloc[0])
print(df.iloc[-1])

print(df.iloc[[0,2,-1]])

print(df.iloc[1:4])
print(df.iloc[::2])

print(df.iloc[[True,False,False,False,False]])