# 02stars_decrease.py

# 별 (*) 을 하나씩 줄여가며 출력하는 프로그램 

i = int(input(">>>몇줄이나 뽑을까요?"))

for n in range ( i + 1, 1, -1) : 
    for m in range (1,n ) :
        print("*", end = '\t')
    print()
