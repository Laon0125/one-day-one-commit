'''
   DataFrame 함수

  1. 기술통계관련 함수
        -최대/최소 값: df["컬럼"].max(axis=0|1), df["컬럼"].min(axis=0|1)
       -최대/최대 레이블: df["컬럼"].idxmax(axis=0|1), df["컬럼"].idxmin(axis=0|1)
       -합계/누적합계: df["컬럼"].sum(axis=0|1), df["컬럼"].cumsum(axis=0|1)
       -평균/중앙값: df["컬럼"].mean(axis=0|1), df["컬럼"].median(axis=0|1)
       -곱/누적곱: df["컬럼"].prod(axis=0|1), df["컬럼"].cumprod(axis=0|1)
       -분산/표준편차: df["컬럼"].var(axis=0|1), df["컬럼"].std(axis=0|1)
       -4분위수: df["컬럼"].quantile(백분율)
       -행 갯수: df["컬럼"].count(axis=0)


'''

import pandas as pd
import numpy as np

df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,15,16,55,4],
                   "c3":[24,25,26,76,3]})
# print(df)
# df.info()
'''
    c1  c2  c3
0  4.0  14  24
1  5.0  15  25
2  6.0  16  26
3  NaN  55  76
4  1.0   4   3
'''
print("1. Series 최대/최소값")
x = df["c2"].max(axis=0)
y = df["c2"].min(axis=0)
print(x, y)

print("2. Series 누적최대/누적최소값")
x = df["c2"].cummax(axis=0)
y = df["c2"].cummin(axis=0)

x = df[["c2","c3"]].cummax(axis=0)
x = df[["c2","c3"]].cummin(axis=0)
print(x, y)

print("3. Series 최대/최소값 레이블")
x = df[["c2","c3"]].idxmax(axis=0)
y = df[["c2","c3"]].idxmin(axis=0)
print(x, y)

print("4. Series 합계/누적합계 - 중요")
x = df[["c2","c3"]].sum(axis=0)
y = df[["c2","c3"]].cumsum(axis=0)
print(x, y)

print("5. Series 평균/중앙값 ")
x = df[["c2","c3"]].mean(axis=0)
y = df[["c2","c3"]].median(axis=0)
print(x, y)

print("5. Series 곱/누적곱 ")
x = df[["c2","c3"]].prod(axis=0)
y = df[["c2","c3"]].cumprod(axis=0)
print(x, y)

print("6. Series 분산/표준편차 ")
x = df[["c2","c3"]].var(axis=0) # variance
y = df[["c2","c3"]].std(axis=0) # standard deviation
print(x, y, np.sqrt(4.666667))

print("7. Series 갯수 ")
x = df[["c2","c3"]].count(axis=0) # 기본적으로 null 제외
print(x)

