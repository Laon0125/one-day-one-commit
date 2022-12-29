# 02dict.py

myDict = {}
myDict2 = {}

# naver www.naver.org
# kakao www.kakao.org

# 2개항목 추가
myDict['naver'] = 'www.naver.org'
myDict2['kakao'] = 'www.kakao.org'

print ( myDict )

myDict['naver'] = 'www.python.org'

print ( myDict )

myDict['google'] = 'www.google.org'

print ( myDict )

myDict.update(myDict2) 

print (myDict)
