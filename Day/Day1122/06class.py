class Test():
    userID='kimyoung' #전역변수
    userPWD='780945'  #전역변수

    def gugudan(self, n):
        for k in range(1,10,1):
            print(f'{n}*{k}={n*k}')
        print('구구단출력끝')
        print(userID)
        print(userPWD)

my = Test() #my객체 = Test클래스명()
my.gugudan(21)



