'''
    pandas의 병합 ( DB 의 조인기능 )

    1. 컬럼 vs 컬럼

    2. 컬럼(df1) vs 인덱스(df2)
        
        pd.merge(df1, df2, left_on = df1컬럼, right_on = df2.index)
        pd.merge(df1, df2, left_on = df1컬럼, right_index = True)

        pd.merge(df2, df1, left_on = df2.index, right_on = df1컬럼)
        pd.merge(df2, df1, left_index = True, right_on = df1컬럼)
    
    
    3. 인덱스 vs 인덱스
        pd.merge(df1, df2,  left_on=df1.index  , right_on=df2.index )
        pd.merge(df1, df2,  left_on=df1.index  , right_index=True )
  

        pd.merge(df2, df1,   left_on=df2.index  , right_on=df1.index )
        pd.merge(df2, df1,   left_on=df2.index  , right_index=True )
        pd.merge(df2, df1,   right_on=df2.index  , left_index=True )
        pd.merge(df2, df1,   right_index=True  , left_index=True )


'''
import numpy as np
import pandas as pd

df1 = pd.DataFrame({"x1":['A',"B",'C','A',"B"],
                    "x2":range(5)})

df2 = pd.DataFrame({"y1":range(3)}, index=list("ABC"))

print (df1)
print (df2)

new_df = pd.merge(df1, df2, left_on= 'x1', right_on = df2.index)
new_df = pd.merge(df1, df2, left_on= 'x1', right_index= True)
new_df = pd.merge(df2, df1, left_on = df2.index, right_on= 'x1')
new_df = pd.merge(df2, df1, left_index= True ,right_on= 'x1')
print(new_df)


