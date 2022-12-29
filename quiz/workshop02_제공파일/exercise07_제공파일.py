

import pandas as pd
import numpy as np
df = pd.read_csv('./workshop02_제공파일/data/food_inspections.csv')
print(df.head())
### 코드 구현 ######
df = df.set_index('DBA Name')
df = df.iloc[[100,1000,10000], [5,3,1]]
print(df)
### 코드 구현 ######