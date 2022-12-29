

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop02_제공파일/data/food_inspections.csv')
print(df.head())
### 코드 구현 ######
'''
제공된 exercise02_제공파일.py 소스파일을 활용하여 다음과 같이 
‘WILD GOOSE BAR & GRILL’ 행만 출력 되도록 코드를 작성하시오.
'''
df = df.set_index("DBA Name")
print(df.loc['WILD GOOSE BAR & GRILL'])
### 코드 구현 ######