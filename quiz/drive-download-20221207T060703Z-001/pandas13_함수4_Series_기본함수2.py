'''
   DataFrame 함수

  2.  함수

    가. 값 변경
        df.replace({old:new, old:new})
        df.replace({"컬럼명":old,...}, new)
        df.replace("컬럼명":{old:new,...})

    나. 레이블 변경
        df.rename(columns={old:new,...})
        df.rename(index={old:new,...})

    다.  모든 값 참이냐/하나라도 참이냐
        ==> np.nan, None 값은 True로 처리됨
         df.all()
         df.any()

     라. 중복조회
        df.duplicated(keep="first|last|False")
        keep="first" ==> 기본값. 처음 발견된 데이터를 기준으로 중복여부체크
        keep="last" ==>  마지막 발견된 데이터를 기준으로 중복여부체크
        keep=Flase  ==>  중복데이터 제외하고 처리

      마. 중복제거후 반환
        df.drop_duplicates()

      바. 임의의 함수 적용
          df.apply(함수, axis=0|1) ==> df의 행과 열이 한번에 함수에 적용됨
'''

import pandas as pd
import numpy as np

df = pd.DataFrame({"k1":['one']*3 + ['two']*4,
                   "k2":[1,1,2,3,3,4,4]})
print(df)
'''
   k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''

print("1. Series 중복된 행이 있냐")
print(df["k1"].duplicated())
print("2. df에 중복된 행 제거후 반환")
# new_df = df["k1"].drop_duplicates()
df.drop_duplicates() # df에는 ignore_index 속성이 지원됨.
new_df = df["k1"].drop_duplicates() # Series에는 ignore_index 속성이 지원안됨.
print(new_df)




df = pd.DataFrame({"c1":[4,5,6,5,1],
                   "c2":[14,15,16,55,4],
                   "c3":[24,25,26,76,3]})

print(df)
print("3. 컬럼별 총합/평균/최대값/최소값")
# df.apply() # df에는 axis가 지원됨.
print(df["c1"].apply(np.sum))  # Series 에는 axis가 지원 안됨.
print(df["c1"].apply(np.mean))
print(df["c1"].apply(np.max))
print(df["c1"].apply(np.min))

'''
    1. 정리 1
    df['c1'] 은 시리즈 반환
    df[['c1']]은 데이터프레임 반환

'''

#########################################################



print("4. df에 지정된 값이 존재하냐?")
df = pd.DataFrame({"c1":[4,5,6,5,1],
                   "c2":[14,15,16,55,4],
                   "c3":[24,25,26,76,3]})
print(df.isin([4,14,1000]))

print("5. df의 특정컬럼에 지정된 값이 존재하냐?")
print(df.isin({"c1":[4,14,1000]}))

df = pd.DataFrame({"c1":[4,5,np.nan,5,1],
                   "c2":[4,15,16,55,4],
                   "c3":[24,25,26,np.nan,np.nan]})
print(df)
'''
    c1  c2    c3
0  4.0   4  24.0
1  5.0  15  25.0
2  NaN  16  26.0
3  5.0  55   NaN
4  1.0   4   NaN
'''
print("6. df의 unique한 갯수(dropna=True 이기때문에 null제거한후에 count함")
print(df['c1'].nunique())

print("6. df의 unique한 갯수(null 포함후에 count함")
print(df['c1'].nunique(dropna=False))



print("7. df에 지정된 값이 존재하냐?")
df = pd.DataFrame({"c1":[4,5,6,5,1],
                   "c2":[14,15,16,55,4],
                   "c3":[24,25,26,76,3]})
print(df['c1'].between(1,4))

print('8. Series의 unique 한 값 반환?')
print(df['c1'].unique())
