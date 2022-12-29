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
df["과학"]=[4,5,6,4,32]
print(df)

# 총함 컬럼 추가
df["총합"]= df["국어"]+df["영어"]+df["수학"]+df["과학"]
print(df)

# 평균 컬럼 추가
df["평균"] = df["총합"] / 4
print(df)

# 합격여부 출력 ( 평균값이 13이상이면 "합격" 아니면 "불합격" 으로 출력 )
df["합격여부"] = ["합격" if avg > 13 else "불합격" for avg in df["평균"] ]
print(df)