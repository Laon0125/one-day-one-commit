import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
df['AGE']= [40,30,35,25,36,44,50]
df['BONUS'] = [10000 if x > 10 else 0 for x in df['YEARS EXPERIENCE']]
df['TOTAL SALALY'] =  (df['SALARY']*1.1).astype(int) + df['BONUS']  
print(df)
# df['TOTAL SALALY'] =  (df['SALARY']*1.1).astype(int) + df['BONUS']
### 코드 구현 ######
