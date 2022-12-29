#07spam.py  

#문제 1~10출력 for반목
#92페이지 리스트 컴프리헨션 구조 
item= [1,2,3,4,5,6,7,8,9,10]
set(item)
for a in item:
    su = a**2
    print(su, end=' ')

print()
for a in range(1,11):
    su = a**2
    print(su, end=' ')

print()

#리스트 컴프리헨션
my = [ i**2 for i in range(1,11)]
print(my)