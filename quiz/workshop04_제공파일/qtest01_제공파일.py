
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
'''
1. 제공된 qtest01_제공파일.py 소스파일을 활용하여 
다음과 같이 출력 되도록 코드를 작성 하시오. ( score값이10이상인행을 5개만출력)
'''

# socre 컬럼 선택
# 값 비교
# 프린트

over_10 = df['score'] >= 10

# 
print(df[over_10].head())
### 코드 구현 ######