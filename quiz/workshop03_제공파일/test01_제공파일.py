
import numpy as np
import pandas as pd

employee = pd.read_csv('./workshop03_제공파일/data/employee.csv')
print(employee.head())
'''
제공된 test01_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 
코드를 작성하시오. ( ‘race’ 컬럼의 빈도수 출력 )
'''
### 코드 구현 ######
'''
1. 제공된 test01_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하 시오. 
( ‘race’ 컬럼의 빈도수 출력 )
'''
print(employee['race'].count())
### 코드 구현 ######