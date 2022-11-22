#92페이지 리스트 컴프리헨션 구조

item = [1,2,3,4,5,6,7,8,9,10]

for a in item :
    su = a **3
    print (su,end=' ')
    su = pow(a,2)
    print (su,end=' ')


for a in range (1,11) :
    su = a **3
    print (su,end=' ')
    su = pow(a,2)
    print (su,end=' ')

print()

my = [i **2 for i in range (1,11)]
print(my)

