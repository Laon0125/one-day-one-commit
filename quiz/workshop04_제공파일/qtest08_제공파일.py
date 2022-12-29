
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
'''
제공된 qtest08_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성 하시오.
( ans_name 값이 null인 행 5개 출력.)
'''
print(df[(df['ans_name'].isnull())].head())


### 코드 구현 ######