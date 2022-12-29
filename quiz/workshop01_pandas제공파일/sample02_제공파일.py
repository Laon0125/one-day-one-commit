

import pandas as pd
import numpy as np

df = pd.read_csv('./workshop01_pandas제공파일/data/sample_data.csv', index_col=0)
print(df)
### 코드 구현 ######
# 제공된 sample02_제공파일.py 소스파일을 활용하여 다음과 같이 color,food,score 3개의 컬럼만 출력 되도록 코드를 작성하시오.
print(df[['color','food','score']])

### 코드 구현 ######