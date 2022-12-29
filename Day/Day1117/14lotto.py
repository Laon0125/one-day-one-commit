#14lotto.py
import random

lotto = set() #{} dict인식
cnt = 0
while True:
    cnt = cnt+1
    num = random.randint(1,45)
    if len(lotto) >= 6:
        break
    else:
        lotto.add(num)

print()
print(lotto)
LT = list(lotto)
LT.sort()
print(LT)
