'''
    pandas의 병합 ( DB의 조인 기능 )

    1. inner 병합(조인)
       - 두 개의 df간에 일치하는 행만 반환

         가. 공통컬럼이 있는 겨우
             pd.merge( df1, df2,  on=공통컬럼 )

        나. 공통컬럼이 없는 경우
             pd.merge( df1, df2,  left_on=df1컬럼 , right_on=df2컬럼 )

    2. outer 병합(조인)
       - 두 개의 df간에 일치하는 행 및 일치하지 않은 행 포함해서 반환

         가. 공통컬럼이 있는 겨우
             pd.merge( df1, df2,  on=공통컬럼 , how="inner(기본)|right|left|outer")

             how="left" ==> 일치하지 않는 df1 행 모두 반환
             how="right" ==> 일치하지 않는 df2 행 모두 반환
             how="outer" ==> 일치하지 않는 df1, df2 행 모두 반환

         나. 공통컬럼이 없는 경우
             pd.merge( df1, df2,  left_on=df1컬럼 , right_on=df2컬럼 , how="inner(기본)|right|left|outer")

'''
import numpy as np
import pandas as pd

df1 = pd.DataFrame({"x1":['A',"B",'C'],
                    "x2":[1,2,3]})

df2 = pd.DataFrame({"y1":['A',"B",'D'],
                    "x3":[10,20,30],
                    "x4":[9,8,6],})

print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  y1  x3  x4
0  A  10   9
1  B  20   8
2  D  30   6
'''
print("2. 공통컬럼이 없는 겨우의 outer 조인 ")
new_df = pd.merge(df1, df2, left_on="x1", right_on="y1", how="left")
new_df = pd.merge(df1, df2, left_on="x1", right_on="y1", how="right")
new_df = pd.merge(df1, df2, left_on="x1", right_on="y1", how="outer")
print(new_df, type(new_df)) # <class 'pandas.core.frame.DataFrame'>