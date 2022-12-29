
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
'''
제공된 qtest04_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성 하시오. 
( score 값이 100이상이거나 answercount 값이 10이상 인 행만 출력)
'''
df = df[(df['score'] >= 100) | (df['answercount'] >= 10)]
print(df)
### 코드 구현 ######