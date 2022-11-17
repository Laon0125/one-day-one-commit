# 01stars_Increase.py

# 별 (*) 을 하나씩 늘려가며 출력하는 프로그램 

i = int(input(">>>몇줄이나 뽑을까요?"))

for n in range ( 1,i+1) : 
    for m in range (1,n + 1) :
        print("*", end = '\t')
    print()
