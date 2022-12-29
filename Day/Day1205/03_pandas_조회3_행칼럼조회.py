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

print ("1. A행 c1컬럼 ")
print(df.loc['A','c1']) #4

print('1. A행, B행 c1칼럼')
print(df.loc[['A','B'],'c1']) #4

print("-"*50)
print('1. A행, C행 c1,c3칼럼')
print(df.loc[['A','C'],['c1','c3']]) #4


print("-"*50)
print('1. b~d행 c1,c3컬럼')
print(df.loc["B":"D",['c1','c3']])



print("-"*50)
print('1. A,C,E 행 c1,c3컬럼')
print(df.loc[[True,False,True,False,True],[True,False,True]])


