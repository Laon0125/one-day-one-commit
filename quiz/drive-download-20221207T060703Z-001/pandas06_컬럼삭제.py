'''
     DataFrame에 컬럼 삭제

     1. 단일컬럼 삭제

        가. df.pop('컬럼명')

        나. del  df['컬럼명']

     2. 다중컬럼 삭제

        df.drop(labels, axis=1)
        df.drop(columns=값)

        def drop(self,
             labels: Hashable | Sequence[Hashable] | None = None, # 삭제할 값(컬럼명,인덱스)
             axis: str | int = 0, # 행/컬럼 지정
            index: Hashable | Sequence[Hashable] | None = None,  # 행삭제
            columns: Hashable | Sequence[Hashable] | None = None, # 컬럼삭제
            level: Hashable | None = None,
           inplace: bool = False,
           errors: Literal["ignore", "raise"] = "raise")
  -> An
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"국어":[4,5,6,4,32],
                   "영어":[14,15,16,5,6],
                   "수학":[24,25,26,3,6],
                   "과학": [4, 5, 6, 4, 32],
                   "체육": [14, 15, 16, 5, 6],
                   "논술": [24, 25, 26, 3, 6],
                   })
print(df)

# 1. 단일컬럼 삭제 - 국어
df.pop("국어")
del df["영어"]
print(df)

# 2. 다중 컬럼 삭제
df.drop(["체육","논술"], axis=1, inplace=True)
df.drop(columns=["과학"], inplace=True)
print(df)


