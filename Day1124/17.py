import numpy as np


a = [ 175, 177, 179, 181, 183 ]
print(a)
print(a[:])
print(a[::2 ]) #시작점 출력 175 179 183
print(a[-1])
print(a[1:4])
print()
jumin='021025-2784306'

back_num = jumin[7:]
print(back_num)
#문제 2 ******-2784306

stra = jumin
stra2 = jumin
a = 0
b = 0
for i in jumin :
    if i == "-" :
        break
    else :
        
        stra = stra[:a] + "*" + stra[a + 1:]
        a += 1

for i in jumin :
    if b > 7 :
        stra2 = stra2[:b] + '*' + stra2[b + 1 :]
        b += 1 
    else :
        b += 1
    

print(stra)
print( stra2)