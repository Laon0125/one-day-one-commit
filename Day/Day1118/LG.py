def book() :
    title = '몽블랑'
    return title

def price() :
    money = 7800 
    return money

def note() :
    print(book)
    print(price)
    print("=" * 50)
    new_Book = book()
    new_Price = price()
    print(new_Book)
    print(new_Price)
    
note()

def myData(name,x,y):
    # 매개변수
    hap = x + y
    avg = hap / 2 

    print('이름 =', name)
    print('총점 =', hap)
    print('평균 =', avg)
