'''
   DataFrame의 인덱스 관리

   1. 인덱스 변경
      ==> 인덱스 기본값은 0 1 2 ... 설정

     가. 새로운 값으로 index 설정
         df.index=[값, ...]

     나. 기존 컬럼값으로 index 설정
        df.set_index("컬럼명")

        def set_index(self,
              keys: Any,
              drop: bool = True, ==> 기존 컬럼값으 삭제하고 인덱스로 지정
              append: bool = False, ==> 기존 인덱스에 새로운 인덱스 추가
              inplace: bool = False, ==> 인덱스 지정된 새로운 복사본 반환

         기존 index --> 컬럼으로 설정
           df.reset_index(drop=False,inplace=True) # 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 설정
           df.reset_index(drop=True,inplace=True)  # 기존 인덱스 삭제하고 새로운 인덱스 설정


     다. 명시적으로 지정된 인덱스를 재배치(순서변경)
         df.reindex(순서변경된인덱스리스트)


     라. DataFrame 연결시 인덱스 제외하고 연결

        new_df = pd.concat([df, df2], ignore_index=True)

'''
import numpy as np
import pandas as pd

df = pd.DataFrame({"date":['2022','2023'],
                   "name":["홍길동","이순신"],
                   "age":[20,30]})

print(df)

# 1. 새로운 값으로 index 설정
df.index = ["사람1","사람2"]
print(df)
print("########################################")
# 2. 기존 컬럼값으로 index 설정
new_df = df.set_index("date", inplace=False, drop=True, append=False)
new_df = df.set_index("date", inplace=False, drop=False, append=False)
new_df = df.set_index("date", inplace=False, drop=True, append=True)
# print(new_df)
df.set_index("date", inplace=True)
print(df)
# df.reset_index(inplace=True)
# df.reset_index(drop=False,inplace=True) # 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 설정
df.reset_index(drop=True,inplace=True)  # 기존 인덱스 삭제하고 새로운 인덱스 설정
print(df)


# 3.명시적으로 지정된 인덱스를 재배치(순서변경)
list_value = np.arange(15).reshape(5,3)
print(list_value)
print(list('DCEAB'))
df = pd.DataFrame(list_value, index=list('DCEAB'))
df.columns=['c1','c2','c3']
print(df)

new_df = df.reindex(["A","B","C","D","E"])
print(new_df)


# 4. DataFrame 연결시 인덱스 제외하고 연결
df = pd.DataFrame({"date":['2022','2023'],
                   "name":["홍길동","이순신"],
                   "age":[20,30]})
df2 = pd.DataFrame({"date":['2024','2025'],
                   "name":["홍길동1","이순신1"],
                   "age":[20,30]})

new_df = pd.concat([df, df2], ignore_index=False)
new_df = pd.concat([df, df2], ignore_index=True)
print(new_df)