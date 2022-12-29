

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./quiz/workshop06_제공파일/data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

print(sp500.head())
### 코드 구현 ######
sp500_copy = None
'''
2. 제공된 df02_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시오. 
( 'RoundedPrice’ 컬럼명으로 데이터프레임 마지막에 추가하고, ‘RoundedPrice2’ 컬 럼명으로 2번째 위치에 삽입한다. 
저장된 데이터는 Price 컬럼값을 반올림한 값으로 저장하고 원본값을 유지하기 위하여 복사본으로 작업한다.)
'''
sp500_copy = sp500
### 코드 구현 ######
print(sp500_copy.head())
# 2.컬럼삽입:  df.insert(컬럼인덱스, 컬럼명, 값)
sp500_copy.insert(1, 'RoundedPrice2', sp500.Price.round() )
print(sp500_copy.head())