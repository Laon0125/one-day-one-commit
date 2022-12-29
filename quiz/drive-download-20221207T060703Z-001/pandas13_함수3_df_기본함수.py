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
new_df = df.replace({24:240, 25:250, 26:260})
print(new_df)

print("2. 값 변경: 지정된 컬럼의 old값을 new값으로 변경")
new_df = df.replace({"c2":26,"c3":24},260)
new_df = df.replace({"c2":[26,55],"c3":[24,76]},260)
print(new_df)

#{'A': {0: 100, 4: 400}}
new_df = df.replace({'c2': {14: 140, 15: 150}})
new_df = df.replace({'c2': {14: 140, 15: 150},'c3':{24:240,25:250}})
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
new_df=df.rename(columns={"c1":"C1","c2":"C2","c3":"C3"})
new_df=df.rename(index={0:"A",1:"B",2:"C",3:"D",4:"E"})
print(new_df)

print("4. df의 모든 컬럼/행이 참이냐?")
# True: None, np.nan, pd.NA ==> True로 처리
# False: 0, "", []
print(df.all(axis=0))
'''
c1     True
c2    False
c3    False
'''
print(df.all(axis=1))
'''
0     True
1     True
2     True
3    False
4    False
'''
print("5. df의 하나라도 컬럼/행이 참이냐?")
# True: None, np.nan, pd.NA ==> True로 처리
# False: 0, "", []
print(df.any(axis=0))
'''
c1    True
c2    True
c3    True
'''
# check
print(df.any(axis=1))
'''
0     True
1     True
2     True
3    False
4     True
'''
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