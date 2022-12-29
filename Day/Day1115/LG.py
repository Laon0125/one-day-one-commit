import time

#LG.py 공급자=제공자입장 서비스제공입장 
def gugudan():
    dan = int(input('구구단을 입력하세요>>> '))
    for c in range(1, 10):
        print(f'{dan} * {c} = {dan*c}')
        time.sleep(1)


user_id='kim7276' #전역변수
user_pwd='encorel234adf'  #전역변수