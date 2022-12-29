'''
   DataFrame 행과 컬럼 조회

    가. 레이블 조회후 값 변경
         -  df.loc[행라벨,  컬럼라벨] = 값
         - 행라벨 지정 형식( 인덱싱,fancy,슬라이싱,불린)
         - 컬럼라벨 지정 형식( 인덱싱,fancy,슬라이싱,불린)

    나. 위치 조회
        -  df.iloc[행위치,  컬럼위치]=값
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
print("1. A행값을 모두 100으로 변경")
df.loc['A']=100
print(df)

print("1. B,C 행값을 모두 200으로 변경")
df.loc[['B','C']]=200
print(df)

print("1. B,D 행  C2, C3 컬럼값 300으로 변경")
df.loc[['B','D'],['c2','c3']]=300
print(df)

print("1. B~D 행  C1~C2 컬럼값 400으로 변경")
df.iloc[1:4, 0:2] = 400
print(df)




