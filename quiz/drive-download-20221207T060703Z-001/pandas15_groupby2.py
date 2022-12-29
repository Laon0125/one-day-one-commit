'''
그룹핑 ( groupby )
    
    1. 기본 문법
     
        df.groupby(by="컬럼명")[컬럼].그룹함수

    2. 그룹함수 한꺼번에 적용

        df.groupby(by="컬럼명")[컬럼].agg([그룹함수,...])

    3. 컬럼별로 그룹함수 지정
        df.groupby(by="컬럼명").agg({

                "컬럼1":['max',"min"],
                "컬럼2":['sum'],

              })
              '''
import numpy as np
import pandas as pd

df = pd.DataFrame({"사원번호":['A1','A2','A3','A4','A5'],
                    "월급":[100,200,150,250,120],
                    "성별":['M',"F","F","M","M"],
                    "부서번호":[10,20,10,20,30]})
print(df)

# 1. 부서별 sal 최대값  
new_df = df.groupby(by="부서번호")['월급'].agg([np.max,np.min,np.sum,np.mean,'count'])
print(new_df)
# print(new_df.to_frame()) # Series --> dataframe 으로 변경

print(df)

# 2. 부서별 성별 월급
new_df = df.groupby(by="부서번호")['월급'].max,min
print(new_df)

new_df = pd.merge(df1, df2, on='부서번호').groupby(by='부서번호')['월급'].['max',"min"]
