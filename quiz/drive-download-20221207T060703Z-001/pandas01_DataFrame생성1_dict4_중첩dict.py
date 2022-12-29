'''

   import pandas as pd
   import numpy as np

    중첩 dict

    { key1:{ key1_1: value},
      key2:{ key2_1: value},
      ..
    }

   ==> 바깥쪽의 key값이 컬럼명으로 지정되고
       안쪽의 key값이 인덱스로 지정된다.

'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"key1":{"key1_1":[4,5,6],"key2_1":[14,15,16],"key3_1":[24,25,26]},
                   "key2":{"key1_1":[4,5,6],"key2_1":[14,15,16],"key3_1":[24,25,26]},
                   "key3":{"key1_1":[4,5,6],"key2_1":[14,15,16],"key3_1":[24,25,26]}
                   })
print(df, type(df))
