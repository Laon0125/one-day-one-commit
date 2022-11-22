class Test:
    userID = 'Kimjw'        #전역변수
    userPWD = 'mdasdkasd'   #전역변수

    def __init__(self,comp,year):
        print('생성자',comp,year)

    def gugudan ( self, n) :
        
        for k in range(1,10,1) :
            print (f'{n}*{k}={n*k}')
        print (n)
        print (self.userID)
        print (self.userPWD)
    
    def note (self) :
        print('note function')

# 구구단 함수 호출
# or
my = Test('엔코아', 2022)
my.gugudan(5)
my.note()