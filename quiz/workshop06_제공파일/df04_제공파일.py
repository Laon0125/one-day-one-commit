

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./quiz/workshop06_제공파일/data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

# print(sp500.head())
sp500.rename(columns={'Book Value': 'BookValue'},
             inplace=True)
sp500_copy = sp500.head().copy()
### 코드 구현 ######
'''
제공된 df04_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시 오. 
( ‘SAMSUNG’ 및 ‘LG’ 인덱스명을 가진 2개의 행을 추가)

'''
new_company = [('Industrials',40.32,12.300 ),('Industrials', 39.20,3.220)]
sp500_copy_new = pd.DataFrame(new_company,columns=sp500_copy.columns, index = ['SAMSUNG', "LG"])

sp500_copy = sp500_copy.append(sp500_copy_new)
print(sp500_copy)