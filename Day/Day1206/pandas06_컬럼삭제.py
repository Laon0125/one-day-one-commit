'''
    DataFrame에 컬럼 삭제

        1. 단일컬럼 삭제
            가. df.pop('컬럼명')
            
            나. del df[]

        2. 다중컬럼 삭제
            df.drop(labels, axis= 0|1)
            df.drop(columns=값)

            labels : single label or list-like
            Index or column labels to drop. A tuple will be used as a single 
            label and not treated as a list-like.

            axis : {0 or 'index', 1 or 'columns'}, default 0
            Whether to drop labels from the index (0 or 'index') or columns
            (1 or 'columns').

            index : single label or list-like
            Alternative to specifying axis (labels, axis=0 is equivalent to 
            index=labels).

            columns : single label or list-like
            Alternative to specifying axis (labels, axis=1 is equivalent 
            to columns=labels).

            level : int or level name, optional
            For MultiIndex, level from which the labels will be removed.

            inplace : bool, default False
            If False, return a copy. Otherwise, do operation 
            inplace and return None.

            errors : {'ignore', 'raise'}, default 'raise'
            If 'ignore', suppress error and only existing labels are dropped.
'''
import numpy as np
import pandas as pd

df = pd.DataFrame({
    '국어': [1,2,3,45,42],
    '영어': [4,5,6,75,76],
    '수학': [7,8,9,101,103],
    '한자': [4,5,6,75,76],
    '사회': [4,5,6,75,76],
    '가정': [4,5,6,75,76],
    '국사': [4,5,6,75,76]}
)
print(df)
'''
   국어  영어   수학  한자  사회  가정  국사
0   1   4    7   4   4   4   4
1   2   5    8   5   5   5   5
2   3   6    9   6   6   6   6
3  45  75  101  75  75  75  75
4  42  76  103  76  76  76  76
'''

# 1. 단일 컬럼 삭제

df.pop('국어')
# df.pop('국어2') #<-- 일치하는 키 없으면 error!
print(df)
'''
   영어   수학  한자  사회  가정  국사
0   4    7   4   4   4   4
1   5    8   5   5   5   5
2   6    9   6   6   6   6
3  75  101  75  75  75  75
4  76  103  76  76  76  76
'''
del df['영어']
print(df)
'''
  수학  한자  사회  가정  국사
0    7   4   4   4   4
1    8   5   5   5   5
2    9   6   6   6   6
3  101  75  75  75  75
4  103  76  76  76  76
'''
# del df['수학', '과학'] <-- 실행불가, 한번에 한개씩만 가능


# 2. 다중컬럼 삭제
df.drop(['한자','국사'],axis=1, inplace=True)
df.drop(columns=['사회'], inplace=True)
print(df)