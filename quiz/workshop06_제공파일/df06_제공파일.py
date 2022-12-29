

import numpy as np
import pandas as pd

np.random.seed(123456)
df = pd.DataFrame({'foo':np.random.random(10000), 'key':range(100, 10100)})
print(df.head())
### 코드 구현 ######
'''
6. 제공된 df06_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시 오. 
( key 컬럼을 새로운 인덱스로 설정하고 10099에 해당되는 foo컬럼값을 출력, foo컬럼 값은 랜덤값이기 때문에 output 값과 일치하지 않는다.)
'''

### 코드 구현 ######
df = df.set_index('key')
print(df)
print(df.loc[10099])
