'''
    정렬
     - 2가지 종류:
        오름차순(기본): 모든 프로그램언어의 기본
        내림차순
     - 다중정렬

    1. df.sort_values()
        - DB의 sql에서 사용할 정렬

        def sort_values(self,
                by: Hashable | Sequence[Hashable], #정렬할 컬럼 정보
                axis: str | int = 0,
                ascending: bool | List[bool] | Tuple[bool, ...] = True, # 오름차순(기본)
                inplace: bool = False,
                kind: str = "quicksort",                            # 정렬 알고리즘
                na_position: str = "last",                          # null값의 위치
                ignore_index: bool = False,
                key: (Series) -> Series | ExtensionArray | ndarray | Index | None = None)
  -> NDFrameT | None


    2. df.sort_index() ==> 위치값이 아니고 레이블 의미

       가. 행의 인덱스(레이블) 정렬
          df.sort_index(axis=0)

        나. 열의 인덱스(레이블) 정렬
          df.sort_index(axis=1)
'''

import numpy as np
import pandas as pd
df = pd.DataFrame({"korea":[14,5,6,np.nan,32],
                   "english":[14,15,16,5,np.nan],
                   "math":[np.nan,25,26,3,6],
                   "science":[4,5,6,34,5]},
                   index=list("BECAD"))
print(df)
'''
   korea  english  math  science
B   14.0     14.0   NaN        4
E    5.0     15.0  25.0        5
C    6.0     16.0  26.0        6
A    NaN      5.0   3.0       34
D   32.0      NaN   6.0        5
'''

# 1. 행 인덱스(레이블) 정렬
new_df = df.sort_index(axis=0)
new_df = df.sort_index(axis=0,ascending=False)
print(new_df)

# 2. 열 인덱스(레이블) 정렬
new_df = df.sort_index(axis=1,ascending=False)
new_df = df.sort_index(axis=1)
print(new_df)