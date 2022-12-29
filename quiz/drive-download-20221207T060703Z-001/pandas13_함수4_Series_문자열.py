'''

    1. python에서 문자열 처리
        예>
            s = 'hello'
            s.함수()

    2. numpy에서 문자열 처리
        예>
            x = np.array{[문자열,문자열]}
            np.char.함수(x)

    3. pandas 에서 문자열 처리

        df['컬럼'].str.함수()

'''

import numpy as np
import pandas as pd

# 1. python에서 문자열 처리
s = 'hello'
print(dir(s))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 


'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
'translate', 'upper', 'zfill']
'''

print(','.join(["A","B","C"]))

# 2. numpy 에서 문자열 처리
print(dir(np.char))

'''
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', '_binary_op_dispatcher',
'_center_dispatcher', '_clean_args', '_code_dispatcher', '_count_dispatcher', 
'_endswith_dispatcher', '_expandtabs_dispatcher', '_get_num_chars', 
'_globalvar', '_join_dispatcher', '_just_dispatcher', '_mod_dispatcher', 
'_multiply_dispatcher', '_partition_dispatcher', '_replace_dispatcher', 
'_split_dispatcher', '_splitlines_dispatcher', '_startswith_dispatcher', 
'_strip_dispatcher', '_to_string_or_unicode_array', '_translate_dispatcher',
'_unary_op_dispatcher', '_use_unicode', '_vec_string', '_zfill_dispatcher',


'add', 'array', 'array_function_dispatch', 'asarray', 'asbytes', 'bool_', 
'capitalize', 'center', 'character', 'chararray', 'compare_chararrays', 
'count', 'decode', 'encode', 'endswith', 'equal', 'expandtabs', 'find', 
'functools', 'greater', 'greater_equal', 'index', 'int_', 'integer', 
'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 
'isspace', 'istitle', 'isupper', 'join', 'less', 'less_equal', 'ljust', 
'lower', 'lstrip', 'mod', 'multiply', 'narray', 'ndarray', 'not_equal', 
'numpy', 'object_', 'overrides', 'partition', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'set_module', 'split', 
'splitlines', 'startswith', 'str_len', 'string_', 'strip', 'swapcase', 
'sys', 'title', 'translate', 'unicode_', 'upper', 'zfill']
'''

x = np.array((['AA','BB']))
print(np.char.lower(x))
print(np.char.capitalize(x))

# 3. pandas 에서 문자열 처리

df = pd.DataFrame({"name":["Hong","park","KIM"],
                   "age":[14,15,26],
                   "address":["seoul","pUsAN","JEJU"]})
print(df)
print(dir(df['name'].str))
'''
['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__frozen', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', '_data', '_doc_args', 
'_freeze', '_get_series_list', '_index', '_inferred_dtype', 
'_is_categorical', '_is_string', '_name', '_orig', '_parent', '_validate', 
'_wrap_result', 


'capitalize', 'casefold', 'cat', 'center', 'contains', 'count', 'decode', 
'encode', 'endswith', 'extract', 'extractall', 'find', 'findall', 
'fullmatch', 'get', 'get_dummies', 'index', 'isalnum', 'isalpha', 
'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 
'isupper', 'join', 'len', 'ljust', 'lower', 'lstrip', 'match', 'normalize', 
'pad', 'partition', 'removeprefix', 'removesuffix', 'repeat', 'replace', 
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'slice', 
'slice_replace', 'split', 'startswith', 'strip', 'swapcase', 'title', 
'translate', 'upper', 'wrap', 'zfill']
'''

df['name'] = df['name'].str.replace('Hong','HONG')
print(df)

df["address"] = df["address"].str.upper()
print(df)
