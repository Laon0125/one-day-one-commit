x = int(input())

def fact(a):
    fact_Num = 1
    for a in range (a,1,-1):
        fact_Num *= a 
    return fact_Num

print(fact(x))