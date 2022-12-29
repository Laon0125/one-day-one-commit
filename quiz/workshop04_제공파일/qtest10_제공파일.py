
import pandas as pd
import numpy as np

# Using [] and .loc for boolean selection
df = pd.read_csv('./workshop04_제공파일/data/stackoverflow_qa.csv')
print(df.head())

### 코드 구현 ######
'''
10. 제공된 qtest10_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성 하시오. 
( viewcount값이 20000보다 큰 행만 10개 출력.
 단, 컬럼은 creationdate, viewcount, ans_name 만 출력한다.)
'''


df = df[
        df['viewcount'] > 20000
    ].head(10)

print(df[["creationdate", 'viewcount', 'ans_name']])

### 코드 구현 ######