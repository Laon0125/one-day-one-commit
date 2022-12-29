"""

    import pandas as pd
    import numpy as np

    DataFrame 생성

    1. dict 이용

        df = pd.DataFrame({key:값, key:값)} # key 가 컬럼으로 지정됨.

    2. 원하는 컬럼순서 변경
        df = pd.DataFrame({key:값, key:값)}

"""
import numpy as np
import pandas as pd

df = pd.DataFrame({ 'c1' : [4,5,6],
                    'c2' : [14,15,16],
                    'c3' : [24,25,26]})

print(df, type(df))

df = pd.DataFrame({ 'c1' : [4,5,6],
                    'c2' : [14,15,16],
                    'c3' : [24,25,26]}, columns=['c2','c3','c1'])
print(df, type(df))