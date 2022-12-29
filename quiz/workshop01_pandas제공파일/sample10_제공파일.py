

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop01_pandas제공파일/data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
'''
제공된 sample10_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작 성하시오.
( Niko 인덱스명을 가진 행의 color, age, score 컬럼값을 각각 ‘RED’, 999, -1 로 변경)
'''
df.loc["niko", ["color","age","score"]] =["RED",999,-1]
print(df)
### 코드 구현 ######
