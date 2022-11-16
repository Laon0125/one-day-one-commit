#14dict.py

a = [7,9,'bc',7,'bc'] # 리스트 순서가 있고 중복이 가능, append 사용 뒤에 추가
b = (7,9,'bc',7,'bc') # 튜플
c = {7,9,'bc',7,'bc'} # 세트 순서도 없고 중복도 허용 x, add 사용 

my = {'python' : 'www.python.com'}
'''
my [키값] = value
naver www.naver.net
kakao www.kakao.org
'''
my['naver'] = 'www.naver.net'
my['kakao'] = 'www.kakao.org'
print(my)
my['naver'] = 'www.apple.com'
print(my)

data = { 1: '버스', 3:'비행기', 4:"택시", 5:'자전거' }
print(data)
data[1] = '지하철'
print(data)
data[2] = 'ktx'
print(data)