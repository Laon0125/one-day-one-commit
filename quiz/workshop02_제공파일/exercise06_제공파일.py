

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop02_제공파일/data/food_inspections.csv')
print(df.head())
### 코드 구현 ######
'''
제공된 exercise06_제공파일.py 소스파일을 활용하여 
다음과 같이 출력 되도록 코드를 작 성하시오. ( 500번째부터 505번째까지의 행 출력 )
'''
df = df.set_index('DBA Name')
df = df.iloc[500:506]
print(df)

### 코드 구현 ######