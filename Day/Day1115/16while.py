# 16while 
# 반복문으로 복귀

su, total = 0, 0

while True:
    su = su + 1
    if su == 5 :
        continue

    print(su, end = " ")
    total = total + su
    if su ==10 :    
        break
    
    

print('총합 = ', total)
print()