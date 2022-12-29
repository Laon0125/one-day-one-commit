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

df = pd.DataFrame({"c1":[4,5,6,4,32],
                   "c2":[14,15,16,5,6],
                   "c3":[24,25,26,3,6],
                   "d1":[24,25,26,3,6]},
                   index=["mouse","rabbit","habbit","mount","hunt"])
print(df)
'''
       c1  c2  c3  d1
mouse    4  14  24  24
rabbit   5  15  25  25
habbit   6  16  26  26
mount    4   5   3   3
hunt    32   6   6   6
'''
print("1. c1 c3 컬럼 조회")
print(df.filter(items=["c1","c3"],axis=1))

print("2. rabbit mount 행 조회")
print(df.filter(items=["rabbit","mount"], axis=0))

print("3. bit 포함된 행 조회")
print(df.filter(like="bit", axis=0))

print("3. c 포함된 컬럼 조회")
print(df.filter(like="c", axis=1))

print("3. t 로 끝나는 행 조회")
print(df.filter(regex="t$", axis=0))

print("3. m 로 시작하는 행 조회")
print(df.filter(regex="^m", axis=0))

print("3. 1~2 로 끝나는 컬럼 조회")
print(df.filter(regex="[1-2]$", axis=1))
