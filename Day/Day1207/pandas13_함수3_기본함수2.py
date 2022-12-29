'''

        라. 중복조회
            df.duplicated(keep='first|last|False')
            keep='first' ==> 기본값. 처음 발견된 값 기준
            keep='last' ==> 마지막에 발견된 값 기준
            keep=False ==> 중복데이터 제외

        마. 중복 제거후 반환

        바. 임의의 함수 적용
            df.apply(함수, axis=)

'''


import numpy as np
import pandas as pd


df = pd.DataFrame({"c1":[1,2,3,4,5],
                   "c2":['one','one','two','two','three']})

print(df.duplicated())

print('2. df 에 중복된 헹 제거 후 반환')

new_df = df.drop_duplicates(ignore_index=True)
print(new_df)

df = pd.DataFrame({"c1":[4,5,6,5,1],
                   "c2":[14,15,16,55,4],
                   "c3":[24,25,26,76,3]})



print(df)
print('3. 컬럼별 총합')
print(df.apply(np.sum, axis= 0))
print(df.apply(np.mean, axis= 0))
print(df.apply(np.max, axis= 0))
print(df.apply(np.min, axis= 0))

df['총합'] = df.apply(np.sum, axis= 1)
df['평균'] = df.apply(np.mean, axis= 1)
df['최대'] = df.apply(np.max, axis= 1)
df['최소'] = df.apply(np.min, axis= 1)
print(df)


df["평균5"]=df['평균'].apply(lambda x:x+5)
print(df)


df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,4,16,55,4],
                   "c3":[24,25,26,76,3]})
print('4. df에 지정된 값이 존재하는가')
print(df.isin([4,14,1000]))

print('5. df에 특정칼럼에 지정된 값이 존재하는가')
print(df.isin({'c1': [4,14,100]}))

print('6 df에 유니크의 개수')
print(df.nunique())

print('6 df에 유니크의 개수 null을 포함해서')
print(df.nunique(dropna=False))

