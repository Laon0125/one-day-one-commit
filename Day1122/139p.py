class Bicycle() :
    #142page

    def __init__(self, name) :
        print(name, ' 대회 출전')
        
    def move(self):
        print('move with bicycle')
        
    def turn (self) :
        pass

    def stop(self) :
        pass
    
print ('Bycicle Class')

my = Bicycle('뚜르드')
my.move()