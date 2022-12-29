
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
'''
6. 제공된 qtest06_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성 하시오. 
( ans_name이 ‘Scott Boston’ 또는 ‘Ted Petrou’ 또는 ‘MaxU’ 또는 ‘unutbu’ 인 행만 출력.)
'''
print (
    df[
        (df['ans_name'] == 'Scott Boston') |
        (df['ans_name'] == 'Ted Petrou') |
        (df['ans_name'] == 'MaxU') | 
        (df['ans_name'] == 'unutbu')
    ].head()
)

### 코드 구현 ######