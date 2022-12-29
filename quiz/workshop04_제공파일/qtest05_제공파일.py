
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
'''
제공된 qtest05_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성 하시오. 
( score 값이 4이상이고 ans_name값이 ‘Scott Boston’ 이거나 answercount 값 이 5이상이고 
ans_name값이 ‘Ted Petrou’ 인 행만 출력 .)
'''
print(df[((df['score'] > 4) & (df['ans_name'] == "Scott Boston"))
| ((df['answercount'] >= 5) & (df['ans_name'] == 'Ted Petrou'))])
### 코드 구현 ######