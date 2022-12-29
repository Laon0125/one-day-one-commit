

import numpy as np
import pandas as pd

sp500 = pd.read_csv("./quiz/workshop06_제공파일/data/sp500.csv",
                    index_col='Symbol',
                    usecols=[0, 2, 3, 7])

# print(sp500.head())
sp500.rename(columns={'Book Value': 'BookValue'},
             inplace=True)
sp500_copy = sp500.head().copy()
new_company = [('Industrials',40.32,12.300 ),('Industrials', 39.20,3.220)]
sp500_copy_new = pd.DataFrame(new_company,columns=sp500_copy.columns, index = ['SAMSUNG', "LG"])
sp500_copy = sp500_copy.append(sp500_copy_new)

### 코드 구현 ######
'''
5. 제공된 df05_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시 오. 
( ‘MMM’ 행은 ‘Sector’,’Price’,’BookValue’ 3개의 컬럼값을 모두 변경하고 ‘ABT’ 행은 ‘Sector’,’Price’ 2개의 컬럼값만 변경한다. 
마지막으로 ‘ABBV’와 ‘ACN’ 행은 삭제시킨다.
변경 데이터는 output 확인하고 df04_제공파일.py 활용)
'''
sp500_copy.loc['MMM'] = ["Information Technology", 100.0, 100.0]
sp500_copy.loc['ABT',['Sector', 'Price']] = ["Information Technology", 100.0]
sp500_copy.drop(['ABBV','ACN'],inplace=True, axis = 0)
print(sp500_copy)



### 코드 구현 ######
print(sp500_copy)