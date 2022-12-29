

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop02_제공파일/data/food_inspections.csv')
print(df.head())
### 코드 구현 ######
df = df.set_index('DBA Name')
'''
제공된 exercise05_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작 성하시오. 
( 인덱스명이 ‘THRESHOLD SCHOOL’ 부터 SCRUB A DUB’ 까지의 행 중에서 step이 3000이고, 
컬럼명이 ‘Inspection Type’ 이후의 모든 컬럼 출력 )
'''
df = df.loc['THRESHOLD SCHOOL':'SCRUB A DUB':3000, 'Inspection Type':]
print(df)
### 코드 구현 ######