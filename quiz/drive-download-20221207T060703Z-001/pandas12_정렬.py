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


    2. df.sort_index()

'''

import numpy as np
import pandas as pd
df = pd.DataFrame({"국어":[14,5,6,np.nan,32],
                   "영어":[14,15,16,5,np.nan],
                   "수학":[np.nan,25,26,3,6],
                   "과학":[4,5,6,34,5]},
                   index=list("BECAD"))
print(df)
print("1. 국어 컬럼으로 오름차순 정렬")
new_df = df.sort_values(by=["국어"])
new_df = df.sort_values(by=["국어"], ascending=False)
new_df = df.sort_values(by=["국어"], ascending=False, na_position="first")
print(new_df)
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
     'col2': [2, 1, 9, 8, 7, 4],
     'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
   })
print(df)
'''
  col1  col2  col3 col4
0    A     2     0    a
1    A     1     1    B
2    B     9     9    c
3  NaN     8     4    D
4    D     7     2    e
5    C     4     3    F
'''
print("2. col1, col2 다중정렬")
new_df = df.sort_values(by=["col1","col2"])
new_df = df.sort_values(by=["col1","col2"], ascending=False)
print(new_df)

print("3. col4 컬럼으로 오름차순 정렬")
new_df = df.sort_values(by=["col4"])
new_df = df.sort_values(by='col4', key=lambda col: col.str.lower())

def xxx(col):
    print(col, type(col)) #  <class 'pandas.core.series.Series'>
    return col.str.lower()
new_df = df.sort_values(by='col4', key=xxx)

print(new_df)
# 외우기 A:65  a:97
print(ord('A'), chr(65))
print(ord('a'), chr(97))