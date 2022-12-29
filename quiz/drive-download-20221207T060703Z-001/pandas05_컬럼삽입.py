'''
     DataFrame에 컬럼 삽입

     df.insert(삽입할컬럼위치,  컬럼명, 값 )

     def insert(self,
           loc: int,
           column: Hashable,
           value: str | float | bool | Period | Period | Timestamp | Timestamp | Timedelta | Timedelta | Interval | Interval | datetime64 | timedelta64 | datetime | ExtensionArray | ndarray | Index | Series,
           allow_duplicates: bool | _NoDefault = lib.no_default) -> None
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"국어":[4,5,6,4,32],
                   "영어":[14,15,16,5,6]})

df.insert(0, "수학", [4,5,6,4,32])
df.insert(1, "수학", [4,5,6,4,32],allow_duplicates=True) # allow_duplicates=False가 기본값
print(df)