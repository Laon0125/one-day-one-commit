'''
   DataFrame 함수

  2.  함수

    가. 값 변경
        df["컬럼"].replace({old:new, old:new})
        df["컬럼"].replace({"컬럼명":old,...}, new)
        df["컬럼"].replace("컬럼명":{old:new,...})

    나. 레이블 변경
        df["컬럼"].rename(columns={old:new,...})
        df["컬럼"].rename(index={old:new,...})

    다.  모든 값 참이냐/하나라도 참이냐
        ==> np.nan, None 값은 True로 처리됨
         df["컬럼"].all()
         df["컬럼"].any()

'''

import pandas as pd
import numpy as np

df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,15,26,55,4],
                   "c3":[24,25,26,76,3]})
print(df)
'''
    c1  c2  c3
0  4.0  14  24
1  5.0  15  25
2  6.0  26  26
3  NaN  55  76
4  1.0   4   3
'''
print("1. 값 변경: 지정된 old값을 new값으로 변경")
new_df = df["c2"].replace({24:240, 25:250, 26:260})
new_df = df[["c2","c3"]].replace({24:240, 25:250, 26:260})
print(new_df)

print()
df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,15,26,pd.NA,0],
                   "c3":[24,25,26,0,3]})
print(df)
'''
    c1    c2  c3
A  4.0  14.0  24
B  5.0  15.0  25
C  6.0  26.0  26
D  NaN   NaN   0
E  1.0   0.0   3
'''
print("3. 레이블(컬럼명/인덱스명) 변경")
new_df=df["c1"].rename("C1")
# new_df=df.rename(index={0:"A",1:"B",2:"C",3:"D",4:"E"})
print(new_df)

print("4. Series 컬럼/행이 참이냐?")
# True: None, np.nan, pd.NA ==> True로 처리
# False: 0, "", []
print(df["c1"].all(axis=0))
# print(df["c1"].all(axis=1)) # df["c1"]==> Series이기 때문에 1차원임. axis=0만 가능함.

print("5. Series 하나라도 컬럼/행이 참이냐?")
# True: None, np.nan, pd.NA ==> True로 처리
# False: 0, "", []
print(df["c1"].any(axis=0))

'''
pd.Series([np.nan]).any()
False
pd.Series([np.nan]).any(skipna=False)
True

pd.Series([np.nan]).all()
True
pd.Series([np.nan]).all(skipna=False)
True
'''