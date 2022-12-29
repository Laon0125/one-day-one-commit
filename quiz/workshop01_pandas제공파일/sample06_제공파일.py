

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop01_pandas제공파일/data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
제공된 sample06_제공파일.py 소스파일을 활용하여
다음과 같이 출력 되도록 코드를 작 성하시오. ( Jane 부터 Penelope 까지의 행과 state, color 컬럼 )
'''
print(df.loc['Jane':'Penelope', ['state','color']])

### 코드 구현 ######