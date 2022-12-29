'''
    2. 함수
        가. 값변경
            df.replace({old:new, old:new})
            df.replace({'컬럼명':old,...},new)
            df.replace({'컬럼명})
            
        나. 테이블 변경
            df.rename(columns={old:new,...})
            df.rename(index={old:new,...})

        

'''
import pandas as pd
import numpy as np


df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,15,26,55,4],
                   "c3":[24,25,26,76,3]})



print('1. 값 변경: 지정된 old값을 새로운 new값으로')
new_df = df['c1'].replace({4:240,5:250,1:260})
print(new_df)
'''
1. 값 변경: 지정된 old값을 새로운 new값으로
    c1   c2   c3
0  4.0   14  240
1  5.0   15  250
2  6.0  260  260
3  NaN   55   76
4  1.0    4    3
'''
print('2. 값 변경: 지정된 old값을 새로운 new값으로')
new_df = df['c1'].replace({'c2':26},260)
print(new_df)
'''
2. 값 변경: 지정된 old값을 새로운 new값으로
    c1   c2  c3
0  4.0   14  24
1  5.0   15  25
2  6.0  260  26
3  NaN   55  76
4  1.0    4   3
'''

print('3. 값 변경: 지정된 old값을 새로운 new값으로')
new_df = df['c1'].replace({'c2':[26,55],'c3':[24,76]},260)
print(new_df)
'''
3. 값 변경: 지정된 old값을 새로운 new값으로
    c1   c2   c3
0  4.0   14  260
1  5.0   15   25
2  6.0  260   26
3  NaN  260  260
4  1.0    4    3
'''

print('3. 값 변경: 지정된 old값을 새로운 new값으로')
new_df = df['c1'].replace({'c2':{14:100,15:150}})
print(new_df)


df = pd.DataFrame({"c1":[4,5,6,np.nan,1],
                   "c2":[14,15,26,np.nan,4],
                   "c3":[24,25,26,0,3]})

print(df)
print('3. 레이블 변경')
new_df = df['c1'].rename('C1')
print(new_df)
'''
3. 레이블 변경
    c1  c2  c3
A  4.0  14  24
B  5.0  15  25
C  6.0  26  26
D  NaN  55  76
E  1.0   4   3
'''

print('4. df의 모든 행/컬럼이 참인가')
# False,'',[],None
print(df['c1'].all(axis=0, skipna=False)) # np.nan or None is True in this case
'''
4. df의 모든 행/컬럼이 참인가
c1    True
c2    True
c3    True
dtype: bool
'''
print('any test')
print(df.any(axis=1, skipna=False))