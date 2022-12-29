'''
    DataFrame의 인덱스 관리
    
    1. 인덱스 변경
        ==> 인덱스 기본값은 0 1 2 ...설정

        가. 
        나. 기존 컬럼값으로 사용
'''

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'date':['2022','2023'],
    'name':['kim','han'],
    'age':[20,30]
})

print(df)

# 1. 새로운 값으로 인덱스 설정
df.index = ['사람1','사람2']
print(df)

# 2. 기존 컬럼값으로 
new_df = df.set_index('date', inplace= False, drop=True, append=False)
'''
date          
2022  kim   20
2023  han   30
'''

new_df = df.set_index('date', inplace= False, drop=False, append=False)
'''
date                
2022  2022  kim   20
2023  2023  han   30
'''
new_df = df.set_index('date', inplace= False, drop=True, append=True)
'''
         name  age
    date          
사람1 2022  kim   20
사람2 2023  han   30
'''
print(df)
print(new_df)
df.set_index("date", inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)
"""  name  age
date          
2022  kim   20
2023  han   30
"""
print(df)
df.reset_index()

# # 3. 명시적으로 지정된 인덱스를 재배치

# list_value = np.arange(15).reshape(5,3)
# print(list_value)

# df = pd.DataFrame(list_value,index= list('DCEAB'))
# df.columns = ['c1','c2','c3']
# print(df)

# new_df = df.reindex(['A','B','C','D','E'])
# print(new_df)


# # 4. DataFrame 연결시 인덱스 제외하고 연결

# df = pd.DataFrame({
#     'date':['2022','2023'],
#     'name':['kim','han'],
#     'age':[20,30]
# })

# df2 = pd.DataFrame({
#     'date':['2024','2025'],
#     'name':['kim1','han1'],
#     'age':[20,30]
# })

# new_df = pd.concat([df,df2],ignore_index=True)
# print(new_df)

