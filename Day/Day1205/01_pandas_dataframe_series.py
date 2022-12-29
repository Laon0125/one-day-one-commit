"""

    DataFrame 생성

    1. Series 생성
        s1 = pd.Series([값,....],name="Series명")
        s2 = pd.Series([값,....],name="Series명")

"""
import numpy as np
import pandas as pd

s1 = pd.Series([1,2,3], name = "sname")
s2 = pd.Series([11,12,13] )
s3 = pd.Series([21,22,23])

print(s1,type(s1))

df = pd.DataFrame([s1,s2,s3], index=["A","B","C"])
columns=["C1","C2","c3"]
print(df)

# Series to DataFrame
s2 = pd.Series([11,12,13])
df2 = s2.to_frame('age')
print(s2)
print(df2, type(df2))