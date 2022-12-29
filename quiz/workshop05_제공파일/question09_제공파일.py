import pandas as pd
import numpy as np

df = pd.read_csv('./workshop05_제공파일/data/employee_sample.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
제공된 question09_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 
코드를 작 성하시오. ( SCORE 컬럼값을 모두 100 으로 변경하고 ‘Niko’, 
‘Penelope’,’Aria’ 인덱스명에 해당되는 FLOOR 컬럼값을 각각 3,6,4 값으로 변경)
'''
df['SCORE'] = 100
df['BONUS_RATE'] = [0.20,0.10,0.00,0.15,0.12,0.30,0.05]
df['FLOOR'] = np.random.randint(1,11,7)
df['LAST_NAME'] = pd.Series(['RM','V','JIN','J-HOPE','JUNGKOOK','SUGAR','JIMIN']).values
df['BONUS'] =  (df['SALARY']*df['BONUS_RATE']).astype(int)
df.loc[['Niko','Penelope','Aria'], ['FLOOR']] = [3,6,4]
print(df)

'''
print('1. A행, B행 c1칼럼')
print(df.loc[['A','B'],'c1']) #4
'''
### 코드 구현 ######