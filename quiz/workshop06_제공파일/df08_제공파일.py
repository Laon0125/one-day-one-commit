

import numpy as np
import pandas as pd
from datetime import datetime

sp500 = pd.read_csv("./quiz/workshop06_제공파일/data/sp500.csv",

                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

'''
8. 제공된 df08_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시 오. 
( Sector값이 ‘Industrials’ 와 ‘Health Care’ 인 행은 삭제하고 반환 )
'''

### 코드 구현 ######
mask = sp500['Sector'].isin(['Industrials', 'Health Care'])
print(sp500[~mask])

### 코드 구현 ######



