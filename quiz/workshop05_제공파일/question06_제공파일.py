import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
6. 제공된 question06_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 
코드를 작 성하시오. ( iloc 함수를 사용하여 3과 5 인덱스 위치에 해당하는 뒤에서 
3번째 컬럼값을 각 각 60과 65로 변경.)
'''

df['AGE']= [40,30,35,25,36,44,50]
df['BONUS'] = [10000 if x > 10 else 0 for x in df['YEARS EXPERIENCE']]
df['TOTAL SALALY'] =  (df['SALARY']*1.1).astype(int) + df['BONUS']  

df.iloc[[3,5],[-3]] = 60, 65
print(df)

### 코드 구현 ######

