

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./quiz/workshop06_제공파일/data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())
### 코드 구현 ######
sp500_copy = None
'''
3. 제공된 df03_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시오. 
( df02_제공파일.py 활용하여 RoundedPrice 컬럼값으로 price컬럼값을 수정하고 RoundedPrice2 컬럼은 삭제한다. )
'''
sp500_copy = sp500
# 2.컬럼삽입:  df.insert(컬럼인덱스, 컬럼명, 값)
sp500_copy.insert(1, 'RoundedPrice2', sp500.Price.round() )
sp500_copy['Price'] = sp500_copy["RoundedPrice2"]
del sp500_copy['RoundedPrice2']
### 코드 구현 ######
print(sp500_copy.head())