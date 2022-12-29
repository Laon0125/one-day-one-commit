

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./quiz/workshop06_제공파일/data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())

### 코드 구현 ######
'''
1. 제공된 df01_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시 오. ( ‘Book Value’ 컬럼명을 ‘BookValue’로 변경 )
'''
sp500.rename(columns={'Book Value':'BookValue'}, inplace=True)
### 코드 구현 ######
print(sp500.head())
