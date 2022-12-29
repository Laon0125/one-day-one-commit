'''
    Series  함수

      1. 기술통계관련 함수
          -최대/최소 값: df.max(axis=0|1), df.min(axis=0|1)
       -최대/최대 레이블: df.idxmax(axis=0|1), df.idxmin(axis=0|1)
       -합계/누적합계: df.sum(axis=0|1), df.cumsum(axis=0|1)
       -평균/중앙값: df.mean(axis=0|1), df.median(axis=0|1)
       -곱/누적곱: df.prod(axis=0|1), df.cumprod(axis=0|1)
       -분산/표준편차: df.var(axis=0|1), df.std(axis=0|1)
       -4분위수: df.quantile(백분율)
       -행 갯수: df.count(axis=0)

       -전체 통계정보 : df.describe()
                      df.info()

       - 지정된 갯수만큼 보기 : df.head(n)
                             df.tail(n)

    df --> df[칼럼명]
'''

import numpy as np
import pandas as pd

df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,15,16,55,4],
                   "c3":[24,25,26,76,3]})

print("1. df 행별(열축) 최대/최소값")
x = df[['c2','c3']].max(axis=0)
y = df[['c2','c3']].min(axis=0)
print(x, y)

print("2. df 행별(열축) 누적최대/누적최소값")
x = df[['c2','c3']].cummax(axis=0)
y = df[['c2','c3']].cummin(axis=0)
print(x, y)

print("3. df 행별(열축) 최대/최소값 레이블")
x = df[['c2','c3']].idxmax(axis=0)
y = df[['c2','c3']].idxmin(axis=0)
print(x, y)

print("4. df 행별(열축) 합계/누적합계 - 중요")
x = df[['c2','c3']].sum(axis=0)
y = df[['c2','c3']].cumsum(axis=0)
print(x, y)

print("5. df 컬럼별(행축) 평균/중앙값 ")
x = df[['c2','c3']].mean(axis=0)
y = df[['c2','c3']].median(axis=0)
print(x, y)

print("5. df 행별(열축) 곱/누적곱 ")
x = df[['c2','c3']].prod(axis=0)
y = df[['c2','c3']].cumprod(axis=0)
print(x, y)

print("6. df 행별(열축) 분산/표준편차 ")
x = df[['c2','c3']].var(axis=0) # variance
y = df[['c2','c3']].std(axis=0) # standard deviation
print(x, y, np.sqrt(4.666667))

print("7. df 행별(열축) 행 갯수 ")
x = df.count(axis=1) # 기본적으로 null 제외
print(x)

