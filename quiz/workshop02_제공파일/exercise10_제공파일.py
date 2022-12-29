

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop02_제공파일/data/stackoverflow_qa.csv')
print(df.head())
### 코드 구현 ######
'''
제공된 exercise10_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작 성하시오. 
( 위의 exercise09_제공파일.py 워크샵 문제에서 id와 score, quest_name, ans_name 컬럼만 출력)
'''

print(df[df['quest_name'] == df['ans_name'] ].head(n = 7)[['id','score','quest_name','ans_name']])


### 코드 구현 ######
