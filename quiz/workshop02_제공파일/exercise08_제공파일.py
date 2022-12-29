

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop02_제공파일/data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######

'''
제공된 exercise08_제공파일.py 소스파일을 활용하여 다음과 같이
 출력 되도록 코드를 작 성하시오. ( answercount 컬럼값이 정확하게 5인 행만 5개만 출력)
'''

print(df[df['answercount'] == 5 ].head())




### 코드 구현 ######
