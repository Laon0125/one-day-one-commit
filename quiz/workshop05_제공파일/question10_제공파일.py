import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
10. 제공된 question10_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 
작 성하시오. ( 부서(DEPARTMENT)명이 ‘ENGINEERING’ 인 사원은 BONUS 값을 
5000 추가로 지급하고 새로운 ‘UPDATE BONUS’ 컬럼에 저장하여 출력)
'''

df['SCORE'] = 100
df['BONUS_RATE'] = [0.20,0.10,0.00,0.15,0.12,0.30,0.05]
df['FLOOR'] = np.random.randint(1,11,7)
df['LAST_NAME'] = pd.Series(['RM','V','JIN','J-HOPE','JUNGKOOK','SUGAR','JIMIN']).values
df['BONUS'] =  (df['SALARY']*df['BONUS_RATE']).astype(int)
df.loc[['Niko','Penelope','Aria'], ['FLOOR']] = [3,6,4]


i = df['DEPARTMENT']=='Engineering'
df['UPDATE_BONUS'] = df['BONUS']
df.loc[i, 'UPDATE_BONUS'] = df[ 'UPDATE_BONUS'] + 5000



print(df)

### 코드 구현 ######