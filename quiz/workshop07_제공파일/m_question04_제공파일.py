
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./quiz/workshop07_제공파일/data/user_usage.csv")
user_device = pd.read_csv("./quiz/workshop07_제공파일/data/user_device.csv")
devices = pd.read_csv("./quiz/workshop07_제공파일/data/android_devices.csv")

### 코드 구현 ######
'''
4. 제공된 m_question04_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시오. 
( user_usage컬럼과 user_device컬럼이 모두 출력되도록 outer merge를 실행 하고 null 값을 포함하는 행의 개수 출력)

'''
result = pd.merge(user_usage,user_device, on='use_id', how="outer")
print(result.shape)
print(result.isna().any(axis=1).sum())
### 코드 구현 ######

