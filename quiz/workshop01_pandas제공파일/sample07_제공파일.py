

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop01_pandas제공파일/data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
제공된 sample07_제공파일.py 소스파일을 활용하여
 다음과 같이 출력 되도록 코드를 작 성하시오. ( 첫 행부터 Dean 까지의 행과 height 부터 마지막 컬럼까지 )
'''

print(df.loc[:'Dean', 'height':])

### 코드 구현 ######