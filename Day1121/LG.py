def getName() :
    name = 'Ko Hee Dong'
    return name

def getPI() :
    pi = 3.1415
    return pi

def note():
    print('note 함수')
    print('*')
    print('**')
    print('***')
    print('****')
    print('*****')

while True :
    print()
    print("1.name 2.이름 3.노트 9.종료")
    sel = int(input('menu select'))

    if sel == 9 :
        break
    elif sel == 1 :
        print(getName())
    elif sel == 2 :
        print(getPI())
    elif sel == 3 :
        note()

