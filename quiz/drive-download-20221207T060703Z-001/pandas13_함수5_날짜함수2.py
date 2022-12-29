'''
    1. 파이썬
        from datetime import datetime

    2. pandas
'''
import numpy as np
import pandas as pd

# 1. 문자를 날짜로 변경
new_date = pd.to_datetime('2022-12-08')
new_date = pd.to_datetime('2022년12월08일', format = '%Y년%m월%d일')
new_date = pd.to_datetime('20221208')
new_date = pd.to_datetime('20221208122530')
print(new_date)

#2. 범위지정해서 날짜 생성
new_date = pd.date_range('2022-11-01','2022-11-10')
new_date = pd.date_range('2022-11-01', periods=5,freq='D')
new_date = pd.date_range('2022-11-01', periods=5,freq='M')
new_date = pd.date_range('2022-11-01', periods=5,freq='Y')
print(new_date)

# 3. df에서 날짜조회
new_date = pd.date_range('2022-11-01', periods=5,freq='D')
df = pd.DataFrame({'날짜':new_date})
print(df)

# 년도/월/일 조사
print(df["날짜"].dt.year)
print(df["날짜"].dt.month)
print(df["날짜"].dt.day)
print(dir(df["날짜"].dt))

