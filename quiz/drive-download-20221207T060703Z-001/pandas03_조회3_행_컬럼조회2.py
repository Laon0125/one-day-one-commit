'''
   DataFrame 행과 컬럼 조회

    가. 레이블 조회
         - 기본문법은  df.loc[행라벨,  컬럼라벨]
         - 행라벨 지정 형식( 인덱싱,fancy,슬라이싱,불린)
         - 컬럼라벨 지정 형식( 인덱싱,fancy,슬라이싱,불린)

    나. 위치 조회
        - 기본문법은  df.iloc[행위치,  컬럼위치]
        - 행위치 지정 형식( 인덱싱,fancy,슬라이싱,불린)
        - 컬럼위치 지정 형식( 인덱싱,fancy,슬라이싱,불린)
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"c1":[4,5,6,4,32],
                   "c2":[14,15,16,5,6],
                   "c3":[24,25,26,3,6]},
                   index=list("ABCDE"))
print(df)
'''
     0   1   2
     c1  c2  c3
0 A   4  14  24
1 B   5  15  25
2 C   6  16  26
3 D   4   5   3
4 E  32   6   6
'''
print("1. A행 c1컬럼")
print(df.iloc[0,0])
print("1. A행, B행  c1컬럼")
print(df.iloc[[0,1],0])

print("1. A행, C행  c1, c3컬럼")
print(df.iloc[[0,2],[0,2]])

print("1. B행~D행  c1, c3컬럼")
print(df.iloc[1:4,[0,2]])

print("1. B행~D행  c2~c3컬럼")
print(df.iloc[1:4,1:])

print("1. A, C, E행  c1, c3컬럼 - 불린색인")
print(df.iloc[[True,False,True,False,True], [True,False,True]]) #
