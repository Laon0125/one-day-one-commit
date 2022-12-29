
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
'''
11. 제공된 qtest11_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성 하시오. 
( favoritecount 값이 30~40 범위에 해당하는 행만 출력. 
단, 컬럼은 title 부터 3 배수에 해당하는 컬럼만 출력)
'''

print(df.loc[df['favoritecount'].between(30,40), 'title'::3])

### 코드 구현 ######