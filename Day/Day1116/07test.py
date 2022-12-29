#07test.py

#숫자발생 로또, 상품권추첨, 지하철 사물함

import random

com_Number = random.randint(1,100)
print('답은', com_Number)
print()



try : 

    for a in range (3) :
        my_Number = int(input('숫자입력 (0을 누르면 종료)>>> ')) 

        if 0 > my_Number or 100 < my_Number :
           print('1 부터 100 까지의 숫자만 넣어주세요')
           
           continue

        if my_Number == com_Number :
            print('빙고! 숫자맞추기 성공띠')
            break

        elif 0 < my_Number < com_Number :
            print(my_Number, ' 당신이 고른 숫자가 더 작습니다')

        elif my_Number > com_Number:
            print(my_Number, ' 당신이 고른 숫자가 더 큽니다')
        
        elif my_Number == 0 :
            print('살려는 드릴께...')
            break
        
        else :
            print('다음 기회에...')
            print('숫자는', com_Number, '이였단다... 못맞췃지롱~~')
    
except ValueError :
    print("숫자만 넣어주세요")


    

print('앙 종료띠~~')
        

