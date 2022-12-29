
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
'''
12. 제공된 qtest12_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성 하시오. 
( answercount 컬럼값이 score 컬럼값보다 큰 행만 출력)
'''
print(
    df[
        (df['answercount'] > df['score'])
    ]
)
 
# 크고 작은 연산가능

### 코드 구현 ######

