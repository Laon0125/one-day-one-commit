

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop01_pandas제공파일/data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
# 1 
print('-'*100)
print(df.index)
# Index(['Jane', 'Niko', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'], dtype='object')
# 2 
print('-'*100)
print(df.columns)
# Index(['state', 'color', 'food', 'age', 'height', 'score'], dtype='object')
# 3 
print('-'*100)
print(df.values)
'''
[['NY' 'blue' 'Steak' 30 165 4.6]
 ['TX' 'green' 'Lamb' 2 70 8.3]
 ['FL' 'red' 'Mango' 12 120 9.0]
 ['AL' 'white' 'Apple' 4 80 3.3]
 ['AK' 'gray' 'Cheese' 32 180 1.8]
 ['TX' 'black' 'Melon' 33 172 9.5]
 ['TX' 'red' 'Beans' 69 150 2.2]]
 '''
### 코드 구현 ######