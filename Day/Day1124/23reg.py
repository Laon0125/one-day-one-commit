import re

s ='Apple is big apple company and apple is very delicious'
k = re.compile('apple', re.I) #compile함수최적화 대소문자무시하고 검색
print(k) #re.compile('apple', re.IGNORECASE)
print(k.findall(s)) 
print(s.find('apple')) #위치
print()
#문제 총문자길이 
print('문자열길이 =', len(s))
print(s.replace('company ', '엔코아 '))
#문제 company 문자열을 엔코아변경
#split(), join(),replace(), len(), find(), 정규식re소속 findAll()

