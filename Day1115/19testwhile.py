# 19testwhile.py
# 1 2 3 4 5
# 6 7 8 9 10... 1 ~ 30

su = 0

while True :
    su = su + 1 
    print (su, end = '\t')

    if su % 5 == 0 :
        print("\n")

    if su == 30 :
        break

