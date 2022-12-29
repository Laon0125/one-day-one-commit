# 03lotto.py
import random
# lotto = []
lotto = set()
cnt = 0

while True :
    cnt = cnt + 1
    num = random.randint(1,45)
    lotto.append(num)
    if cnt == 6:break

print ()
print(lotto)