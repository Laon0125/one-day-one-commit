u = '<<<      spam<><> and ham >>>'
print(u)
print()

#문제 < > <> 특문제거 strip(), lstrip(), rstrip()
#문제 replace() 사용 spam --> tomato and egg
#문제 단어word 로 쪼개기 split 함수

data = u.replace("<", ' ')
data = data.replace(">", ' ')
print("1번", data)

data = data.replace('spam', 'egg and tomato')
print('2번',data)

data = data.split()
print(data)
