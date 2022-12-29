

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop01_pandas제공파일/data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
제공된 sample09_제공파일.py 소스파일을 활용하여
 다음과 같이 출력 되도록 코드를 작 성하시오. ( age가 30보다 작은 행의 score값을 99로 변경)
'''
df.loc[df['age']<30,"score"]=99
print(df)

### 코드 구현 ######