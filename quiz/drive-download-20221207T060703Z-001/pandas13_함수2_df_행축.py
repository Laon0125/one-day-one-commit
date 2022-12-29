'''
   DataFrame 함수

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




'''

import pandas as pd
import numpy as np

df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,15,16,55,4],
                   "c3":[24,25,26,76,3]})
print(df)
df.info()
'''
    c1  c2  c3
0  4.0  14  24
1  5.0  15  25
2  6.0  16  26
3  NaN  55  76
4  1.0   4   3
'''
print("1. df 컬럼별(행축) 최대/최소값")
x = df.max(axis=0)
y = df.min(axis=0)
print(x, y)

print("2. df 컬럼별(행축) 누적최대/누적최소값")
x = df.cummax(axis=0)
y = df.cummin(axis=0)
print(x, y)

print("3. df 컬럼별(행축) 최대/최소값 레이블")
x = df.idxmax(axis=0)
y = df.idxmin(axis=0)
print(x, y)

print("4. df 컬럼별(행축) 합계/누적합계 - 중요")
x = df.sum(axis=0)
y = df.cumsum(axis=0)
print(x, y)

print("5. df 컬럼별(행축) 평균/중앙값 ")
x = df.mean(axis=0)
y = df.median(axis=0)
print(x, y)

print("5. df 컬럼별(행축) 곱/누적곱 ")
x = df.prod(axis=0)
y = df.cumprod(axis=0)
print(x, y)

print("6. df 컬럼별(행축) 분산/표준편차 ")
x = df.var(axis=0) # variance
y = df.std(axis=0) # standard deviation
print(x, y, np.sqrt(4.666667))

print("7. df 컬럼별(행축) 행 갯수 ")
x = df.count(axis=0) # 기본적으로 null 제외
print(x)

print("8. df 컬럼별(행축) 사분위수 ")
x = df.count(axis=0) # 기본적으로 null 제외
print(x)

# 사분위수
df = pd.DataFrame({"price":[10,20,30,40,1,2,3,4,5]})
print(df, sorted(df['price'])) # [1, 2, 3, 4, 5, 10, 20, 30, 40]

print("9. 2사분위(50%) 구하기")
x = df.quantile(0.5)
print(x)

print("10. 1, 2, 3사분위(25%, 50%, 75%) 구하기")
x = df.quantile([0.25, 0.5, 0.75])
print(x)

print("11. 3사분위와 1사분위 차(IQR) 구하기")
x = df.quantile(0.75)-df.quantile(0.25)
print(x)

print("12. df 통계정보 ")
x = df.describe()
print(x)
df.info()

print("13. df의 지정된 상위 행갯수만큼 보기 ")
x = df.head()
x = df.head(2)
print(x)

print("14. df의 지정된 하위 행갯수만큼 보기 ")
x = df.tail()
x = df.tail(2)
print(x)

