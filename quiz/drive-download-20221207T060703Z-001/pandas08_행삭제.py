'''
     DataFrame에 컬럼 삭제

     1.  단일/다중 행 삭제

        df.drop(labels, axis=0)
        df.drop(index=값)

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
                   }, index=list("ABCDE"))

print(df)

df.drop(["A","B"], inplace=True, axis=0)
print(df)

df.drop(index=["D","E"], inplace=True)
print(df)


