'''

   import pandas as pd
   import numpy as np

   DataFrame 생성

   1. Series 생성

      s1 = pd.Series([값,...], name="Series명")
      s2 = pd.Series([값,...], name="Series명")

      df = pd.DataFrame([s1, s2,...])

'''
import numpy as np
import pandas as pd

s1 = pd.Series([1,2,3], name="sname")
s2 = pd.Series([11,12,13])
s3 = pd.Series([21,22,23])
print(s1, type(s1))

# df = pd.DataFrame([s1, s2, s3], index=["A","B","C"], columns=["c1","c2","c3"]) ==> 기존컬럼의 순서 변경
df = pd.DataFrame([s1, s2, s3], index=["A","B","C"])
df.columns=["c1","c2","c3"]
print(df)
'''
   c1  c2  c3
A   1   2   3
B  11  12  13
C  21  22  23
'''
# transpose()
print(df.T)
'''
    A   B   C
c1  1  11  21
c2  2  12  22
c3  3  13  23
'''

# Series --> DataFrame
s2 = pd.Series([11,12,13])
df2 = s2.to_frame("age")
print(s2, type(s2))
print(df2, type(df2))