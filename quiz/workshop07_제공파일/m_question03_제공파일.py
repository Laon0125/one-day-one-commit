
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./quiz/workshop07_제공파일/data/user_usage.csv")
user_device = pd.read_csv("./quiz/workshop07_제공파일/data/user_device.csv")
devices = pd.read_csv("./quiz/workshop07_제공파일/data/android_devices.csv")


### 코드 구현 ######
'''
3. 제공된 m_question03_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시오. 
( 앞의 m_question01_제공파일.py 의 merge작업은 user_device 데이터프레 임에서 누락된 데이터가 발생된다. 
따라서 outer 작업으로 merge 하여 모든 user_ device 데이터를 출력하도록 한다.)
'''
result = pd.merge(user_usage,user_device, on='use_id', how="right")
### 코드 구현 ######
print(result.head())
### 코드 구현 ######
print(result.shape)
print(result['monthly_mb'].isna().sum())
print(result['platform'].isna().sum())

### 코드 구현 ######
