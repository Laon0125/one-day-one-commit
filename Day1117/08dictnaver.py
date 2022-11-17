#08dictnaver.py 

mydict = { }
mydict['naver'] = 'www.naver.org'
mydict['kakao'] = 'www.kakao.com'
mydict['python'] = 'www.python.org'

#for반복문  enumerate(딕션이름)
cnt = 0 
for k in mydict:
    print(cnt, ' ',k, ':',  mydict[k])
    cnt = cnt + 1



print()
'''
for k in mydict:
    #print(k)
    print(k, ':',  mydict[k])
naver   www.naver.org
kakao   www.kakao.com
python  www.python.org


cnt = 0 
for k in mydict:
    print(cnt, ' ',k, ':',  mydict[k])
    cnt = cnt + 1
0  naver   www.naver.org
1  kakao   www.kakao.com
2  python  www.python.org
'''  