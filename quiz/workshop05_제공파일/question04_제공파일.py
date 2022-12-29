import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
4. 제공된 question04_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 
코드를 작성하시오. ( Aria 인덱스명에 해당하는 부서(department)컬럼값을 
‘Police’로 변경 )
'''
df.loc[['Aria'],['DEPARTMENT']] = "Police"
print(df)
'''
df.loc[['B', 'C']] = 200
'''
### 코드 구현 ######

