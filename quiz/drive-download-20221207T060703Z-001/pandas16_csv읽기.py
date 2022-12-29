'''

    파일 I/O
    
    1. csv파일 읽기

        csv는 , 로 구분된  데이터로 된 파일을 처리


'''
import pandas as pd
import numpy as np
df = pd.read_csv('./data/msft.csv',encoding= 'utf-8')

# 1. 컬럼을 인덱스로 변경
new_df = pd.read_csv('./data/msft.csv',index_col = 0)

# 2. 컬럼명 변경
new_df = pd.read_csv('./data/msft.csv',header=0,names=[])

# 3. 지정된 칼럼만 읽기

new_df = pd.read_csv('./data/msft.csv',usecols=['Date', 'Open'])
new_df = pd.read_csv('./data/msft.csv',usecols=[0,1,2])

# 4. 지정된 행 개수만큼만 가져오기
new_df = pd.read_csv('./data/msft.csv',nrows=4)
print(new_df)
new_df.to_csv('./data/custom_out.csv')

