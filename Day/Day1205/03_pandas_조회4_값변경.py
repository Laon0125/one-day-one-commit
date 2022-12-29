'''
    dataframe 횅과 컬럼 조회

        가. 레이블 조회
            - 기본문법은 df.loc[행라벨, 컬렘라벨]
            - 행라벨, 지정형식 (인덱싱 facny slice boolean)
            - 열라벨, 지정형식 (인덱싱 facny slice boolean)
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

print ("1. A행 값을 모두 100으로 변경 ")
df.loc["A"]=100 
print(df)

print('1. B행, C행 값을 모드 200으로 변경')
df.loc[['B', 'C']] = 200
print(df) 

print("-"*50)
print('1. b,d c2,c3 값 모두 300')
df.iloc[[1,3],[1,2]] = 300
print(df)


print("-"*50)
print('1. b~d행 c1~c2열 값 변경')
df.iloc[1:4,0:2] = 400
print(df)



print("-"*50)
print('1. A,C,E 행 c1,c3컬럼')
print(df.iloc[[True,False,True,False,True],[True,False,True]])


