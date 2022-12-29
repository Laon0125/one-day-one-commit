import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
5. 제공된 question05_제공파일.py 소스파일을 활용하여 
다음과 같이 출력 되도록 코드를 작 성하시오. 
( 인종(race)이 ‘white’ 이고 부서(department)명이 ‘Engineering’ 인 사원은 
salary에 10000을 더하고, 
인종(race)이 ‘black’ 이고 부서(department)이 ‘parks & Recreation’ 인 사원은 
salary에 20000을 더한다.)
'''
'''
이거쓰면 두 조건 충족하는 사람 출력
df[(df["RACE"]=='White')&(df['DEPARTMENT']=='Engineering')]

'''

i = (df["RACE"]=='White')&(df['DEPARTMENT']=='Engineering')
j = (df["RACE"]=='Black')&(df['DEPARTMENT']=='Parks & Recreation')


df.loc[i,'SALARY'] = df["SALARY"] + 10000
df.loc[j,'SALARY'] = df["SALARY"] + 20000
print(df)

### 코드 구현 ######

