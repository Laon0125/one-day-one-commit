'''
     DataFrame에 컬럼 추가

     1.
       df["새로운컬럼"]=값(리스트)

     2. df.assign(컬럼명=리스트, 컬럼명=리스트,...)

     3. df와 df2 연결
        pd.concat()
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"국어":[4,5,6,4,32],
                   "영어":[14,15,16,5,6],
                   "수학":[24,25,26,3,6]})
print(df)

# 1. 과학 컬럼 추가
df = df.assign(과학=[4,5,6,4,32])
print(df)

# 총함 컬럼 추가
# df = df.assign(총합=df["국어"]+df["영어"]+df["수학"]+df["과학"])
def total_sum(df):
    return df["국어"]+df["영어"]+df["수학"]+df["과학"]

total_sum2 = lambda df:df["국어"]+df["영어"]+df["수학"]+df["과학"]
df = df.assign(총합=total_sum2)

df = df.assign(총합2=lambda df:df["국어"]+df["영어"]+df["수학"]+df["과학"])
print(df)

# 평균 컬럼 추가 ==> 일반함수 및 lambda로 추가하시오
def avg(df):
    return df["총합"]/4
df = df.assign(평균=avg)
print(df)

df = df.assign(평균2=lambda dv:df["총합"]/4)
print(df)

# 합격여부 출력 ==> lambda로 추가하시오
df = df.assign(합격여부=lambda dv:["합격" if avg > 13 else "불합격" for avg in df["평균"]])
print(df)