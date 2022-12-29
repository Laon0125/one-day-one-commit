import pandas as pd
import numpy as np
import random
df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
8. 제공된 question08_제공파일.py 소스파일을 활용하여 다음과 같이 출력 
되도록 코드를 작 성하시오. 
( 1~10 범위의 랜덤 정수값이 저장된 ‘FLOOR’ 컬럼을 추가하고 pd.Series 객체 를 사용하여
 ‘LAST NAME’ 컬럼을 추가한다. 
 마지막으로 ‘BONUS RATE’ 컬럼과 ‘SALARY’ 컬럼을 곱셈한 결과를 
 ‘BONUS’ 컬럼을 생성하고 정수형으로 저장한다. 저장된 데이터는 output 참조)
'''
df['SCORE'] = 99
df['BONUS_RATE'] = [0.20,0.10,0.00,0.15,0.12,0.30,0.05]
df['FLOOR'] = np.random.randint(1,11,7)
df['LAST_NAME'] = pd.Series(['RM','V','JIN','J-HOPE','JUNGKOOK','SUGAR','JIMIN']).values
df['BONUS'] =  (df['SALARY']*df['BONUS_RATE']).astype(int)
print(df)


### 코드 구현 ######