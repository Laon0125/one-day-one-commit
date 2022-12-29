
import pandas as pd
import numpy as np

user_usage = pd.read_csv("./quiz/workshop07_제공파일/data/user_usage.csv")
user_device = pd.read_csv("./quiz/workshop07_제공파일/data/user_device.csv")
devices = pd.read_csv("./quiz/workshop07_제공파일/data/android_devices.csv")

print("user_usage 데이터프레임: \n", user_usage)
print("user_device 데이터프레임: \n",user_device)
print("devices 데이터프레임: \n",devices)

result = None
### 코드 구현 ######
'''
1. 제공된 m_question01_제공파일.py 소스파일을 활용하여 다음과 같이 출력 되도록 코드를 작성하시오. 
( 먼저 android_devices.csv의 ‘Retail Branding’ 컬럼명을 ‘manufacturer’로 변 경하여 출력하고, user_usage와 
user_device 데이터프레임을 공통컬럼인 ‘use_id’ 사용하 여 merge 하여 출력한다. )
'''
devices.rename(columns={'Retail Branding':'manufacturer'}, inplace=True)
print(devices.head())
result = pd.merge(user_usage,user_device, on='use_id')
### 코드 구현 ######
print(result.head())

