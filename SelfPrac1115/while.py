#while.py
'''
while 조건문에
and 가 들어갈떄와
or 이 들어갈떄의 
차이를 보기위한 예제
'''

import time
#변수 a, b 선언
a, b = 0, 0

while a <10 and b < 10 :
    
    a = a + 1 
    b = a + 1
    time.sleep(1)
    print(a,"\t", b)

print('while and end')

a, b = 0, 0

while a <10 or b < 10 :
    
    a = a + 1 
    b = a + 1
    time.sleep(1)
    print(a,"\t", b)

print('while or end')