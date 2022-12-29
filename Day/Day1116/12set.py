#12set.py

a = [7,9,'bc',7,'bc'] # 리스트 순서가 있고 중복이 가능, append 사용 뒤에 추가
b = (7,9,'bc',7,'bc') # 튜플
c = {7,9,'bc',7,'bc'} # 세트 순서도 없고 중복도 허용 x, add 사용 

a.append('core')
print(a)

c.add('core')
print(c)