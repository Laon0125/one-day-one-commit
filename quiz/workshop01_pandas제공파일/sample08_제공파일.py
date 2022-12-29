

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop01_pandas제공파일/data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
제공된 sample08_제공파일.py 소스파일을 활용하여
다음과 같이 출력 되도록 코드를 작 성하시오. ( height 값이 170 이상인 행과 state, height, score 컬럼만 출력)
'''
print(df.loc[df['height']>=170, ['state','height','score']])

### 코드 구현 ######