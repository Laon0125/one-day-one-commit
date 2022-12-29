import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
1. 제공된 question01_제공파일.py 소스파일을 활용하여 
다음과 같이 출력 되도록 코드를 작성하시오. ( 새로운AGE컬럼을추가)
'''

df['AGE']= [40,30,35,25,36,44,50]
print(df)
### 코드 구현 ######