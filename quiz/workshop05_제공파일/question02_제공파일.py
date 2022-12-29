import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
2. 제공된 question02_제공파일.py 소스파일을 활용하여 다음과 같이 출력되도록 코드를 작성하시오. 
( 새로운 BONUS 컬럼을 추가하고 ‘YEARS EXPERIENCE’ 값이 10 보다 크면 BONUS 컬럼에 10000 
값을 저장한다. 이때 원본을 유지하기 위하여 새로운 df_orig 변수 에 원본을 저장한 후에 작업한다.)
'''
df['AGE']= [40,30,35,25,36,44,50]
df['BONUS'] = [10000 if x > 10 else 0 for x in df['YEARS EXPERIENCE']]
print(df)
### 코드 구현 ######