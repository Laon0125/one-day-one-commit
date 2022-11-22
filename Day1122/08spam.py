#92 페이지 참고

massege = [ 'spam', 'ham','spam','spam','ham']

#ham 데이터만 추출

for i in massege :
    if i == "ham" :
        print("ham")

data = [i for i in massege if i == 'ham']
print(data)

# 람다식 클래스안에서 함수(self) 리스트 컴프리헨션 복습하기