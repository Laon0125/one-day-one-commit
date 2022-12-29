"""
    중첩 dict
    { key2: {key1_1: value},
      key2: {key2_1: value},
      ..
      
    }
  
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'key1': {'key1_1':[3,4,5],'key2_1':[3,4,5],'key3_1':[3,4,5]},
    'key2': {'key2_1':[3,4,5]},
    'key3': {'key3_1':[3,4,5]}
})

# 1. 원본
print(df, type(df))
