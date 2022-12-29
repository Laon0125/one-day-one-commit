# df.filter()
'''
   DataFrame 행과 컬럼 조회

     df.filter()

     def filter(self: NDFrameT,
           items: Any = None,  ==> 검색항목 지정
           like: str | None = None,  ==> 비슷한 값 반환
           regex: str | None = None, ==> 정규표현식
           axis: Any = None)    ==> 0:행 1:열

     * 정규표현식(regular expression)
       - 일정한 패턴을 지정해서 패턴과 일치하는 문자열을 조회
       - 자바, 자바스크립트, 파이썬 지원

'''

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'c1': [1,2,3,45,42],
    'c2': [4,5,6,75,76],
    'c3': [7,8,9,101,103],
    'd1': [7,8,9,101,103]},
    index= ['mouse', 'rabbit', 'mount','habbit','hunt' ]
    )

print(df)
'''
        c1  c2   c3   d1
mouse    1   4    7    7
rabbit   2   5    8    8
mount    3   6    9    9
habbit  45  75  101  101
hunt    42  76  103  103
'''



print("1. c1 c3칼럼 조회")
print(df.filter(items=['c1','c3'],axis = 1))
'''
1. c1 c3칼럼 조회
        c1   c3
mouse    1    7
rabbit   2    8
mount    3    9
habbit  45  101
hunt    42  103
'''

print('2. rabbit, mount 행 조회')
print(df.filter(items=["rabbit",'mount'],axis=0))
'''
2. rabbit, mount 행 조회
        c1  c2  c3  d1
rabbit   2   5   8   8
mount    3   6   9   9
'''

print('3. bit 포함 헹 조회')
print(df.filter(like='bit', axis=0))
'''
3. bit 포함 헹 조회
        c1  c2   c3   d1
rabbit   2   5    8    8
habbit  45  75  101  101
'''

print('3. c 포함 컬럼 조회')
print(df.filter(like='c', axis=1))
'''
3. c 포함 컬럼 조회
        c1  c2   c3
mouse    1   4    7
rabbit   2   5    8
mount    3   6    9
habbit  45  75  101
hunt    42  76  103
'''

print('3.t로 끝나는 행 조회')
print(df.filter(regex='t$', axis=0))
'''
3.t로 끝나는 행 조회
        c1  c2   c3   d1
rabbit   2   5    8    8
mount    3   6    9    9
habbit  45  75  101  101
hunt    42  76  103  103
'''

print('3.m로 시작하는 행 조회')
print(df.filter(regex='^m', axis=0))
'''
3.m로 시작하는 행 조회
       c1  c2  c3  d1
mouse   1   4   7   7
mount   3   6   9   9
'''

print('3.1~2로 끝나는 컬럼 조회')
print(df.filter(regex='[1~2]$', axis=1))
'''
3.1~2로 끝나는 컬럼 조회
        c1  c2   d1
mouse    1   4    7
rabbit   2   5    8
mount    3   6    9
habbit  45  75  101
hunt    42  76  103
'''