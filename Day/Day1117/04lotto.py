# 04lotto.py
import random
lotto = set()
cnt = 0

while True :
    num = random.randint(1,45)
    if len(lotto) >=6:
        break
    else :
        lotto.add(num)

print ()
print(lotto)
LT = list(lotto)
LT.sort()
print(LT)