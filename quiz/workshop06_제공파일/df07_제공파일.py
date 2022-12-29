

import numpy as np
import pandas as pd
from datetime import datetime
import random

### 코드 구현 ######
'''
7. 제공된 df07_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시오. 
( 생성한 DataFrame의 foo컬럼은 5개의 랜덤값으로 설정하고 bar컬럼은 10 ~ 14까지 의 순서값으로 설정한다. 
인덱스는 날짜데이터로 설정하고 현재날짜부터 출력한다. 실행 시점에 따라서 날짜값은 달라질 수 있으며 지정된 포맷을 사용한다.)
'''
today = str(datetime.today())[:10]
print(today)
new_date = pd.date_range(today, periods=5,freq='D')
foo = np.random.rand(5) 
bar = [10,11,12,13,14]
data = {'foo':foo, 'bar':bar}
df = pd.DataFrame(data,index=new_date)
print(df)
### 코드 구현 ######



