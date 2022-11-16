#11testCoffee

money = 0
flag = True
sel = 0
coffee_Price = 300
coco_Price = 250

money = int(input('동전투입>>> '))
while flag:
    print('======= 자판기 프로그램 =======')
    print('1.커피(300원) 2.코코아(250원) 3.반환 9.종료')
    sel = int(input('메뉴선택>>>'))
    if sel == 9 :
        print(money, '원 남았다냥~~ ')
        print('고맙다냥~ 또 오라냥~~')
        break
    elif sel == 1 :
        if money >= coffee_Price :
            money -= coffee_Price
            print('주문하신 커피 나와다냥~~ 남은 돈은 ' , money , "원 이다냥")
        else :
            print('돈이 부족하다냥~~')
    
    elif sel == 2 :
        if money >= coco_Price :
            money -= coco_Price
            print('따뜻한 코코아가 나왔다냥~~ 남은 돈은 ', money , "원 이다냥")
        else :
            print('돈이 부족하다냥~~')
    elif sel == 3 :
        print(money, '원 남았다냥~~ 잘가라냥~~')
        break
    



    