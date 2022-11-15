import random
import time

face = 1
tail = 0
n = 0
face_Count = 0
tail_Count = 0

while n < 1000000 :
    coin = random.randint(0,1)
    n = n + 1
    if coin == face :
        print('앞면')
        face_Count = face_Count + 1

    else :
        print('뒷면')
        tail_Count = tail_Count + 1

print (face_Count," ", tail_Count)

