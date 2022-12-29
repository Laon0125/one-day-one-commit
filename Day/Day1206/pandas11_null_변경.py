'''
    null 변경

    1. 임의의 값으로 변경 (평균값, 중앙값)

        df.fillna(임의의 값)

    2. null 앞에있는값, 뒤에있는값 으로 변경

        df.fillna(method='ffill) ==> 앞에있는 값으로 치환
        df.fillna(method='bfill) ==> 뒤에있는 값으로 치환
        
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({"국어":[4,5,6,np.nan,32],
                   "영어":[14,15,16,5,np.nan],
                   "수학":[np.nan,25,26,3,6],
                   "과학":[4,5,6,34,5]})

print(df)
'''     국어    영어    수학  과학
0   4.0  14.0   NaN   4
1   5.0  15.0  25.0   5
2   6.0  16.0  26.0   6
3   NaN   5.0   3.0  34
4  32.0   NaN   6.0   5

'''

print('1. 모든 null값을 임의의 값으로 저장')
new_df = df.fillna(0)
print(new_df)

'''
     국어    영어    수학  과학
0   4.0  14.0   0.0   4
1   5.0  15.0  25.0   5
2   6.0  16.0  26.0   6
3   0.0   5.0   3.0  34
4  32.0   0.0   6.0   5
'''

print('2. 컬럼단위로 null값을 임의값으로 변환')
new_df = df.fillna({'국어':0,'영어':-10,'수학':-20})
print(new_df)
'''
     국어    영어    수학  과학
0   4.0  14.0 -20.0   4
1   5.0  15.0  25.0   5
2   6.0  16.0  26.0   6
3   0.0   5.0   3.0  34
4  32.0 -10.0   6.0   5
'''


df = pd.DataFrame({"국어":[4,5,6,np.nan,32],
                   "영어":[14,np.nan,16,5,10],
                   "수학":[52,np.nan,25,26,3],
                   "과학":[4,5,6,34,5]})
print(df)

new_df = df.fillna(method='ffill')
print(new_df)


new_df = df.fillna(method='bfill')
print(new_df)