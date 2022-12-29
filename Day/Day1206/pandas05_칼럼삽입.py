import numpy as np
import pandas as pd

df = pd.DataFrame({
    '국어': [1,2,3,45,42],
    '영어': [4,5,6,75,76]}
)

df.insert(0,'수학',[4,5,6,7,8])

# 만약 이름이 같은 키로 중복된 열을 만들려면 allow_duplicate= True 를 주어야 한다
df.insert(1,'수학',[4,3,7,4,2],allow_duplicates=True) 
print(df)