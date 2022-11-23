#08spam.py  

#92페이지 리스트 컴프리헨션 축약식
message =  [  'spam', 'ham', 'spam', 'spam', 'ham' ]
#ham데이터추출 
for k  in message:
    if k=='ham':
        print(k, end='  ')

print()
data = [ i for i in message if i=='ham']
print(data)

#람다식, 클래스안에서 함수(self)