import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''

7. 제공된 question07_제공파일.py 소스파일을 활용하여 
다음과 같이 출력 되도록 코드를 작 성하시오. 
( ‘SCORE’ 컬럼 및 ‘BONUS RATE’ 컬럼 추가. 저장 데이터는 output 참조)
'''

df['SCORE'] = 99
df['BONUS_RATE'] = [0.20,0.10,0.00,0.15,0.12,0.30,0.05]
print(df)

### 코드 구현 ######