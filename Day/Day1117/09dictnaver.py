# 09dictnaver.py
mydict = {}
mydict ['naver'] = 'www.naver.org'
mydict ['kakao'] = 'www.kakao.org'
mydict ['python'] = 'www.python.org'
mydict ['gg'] = 'www.google.org'

mylist_keys = list(mydict.keys())
mylist_values = list(mydict.values())

#for 반복문 enumerate(딕션이름)
for index,a in enumerate(mydict) :
    print(' ', a, ':', mydict[a])

for a,b in mydict.items :
    print(a,b)
