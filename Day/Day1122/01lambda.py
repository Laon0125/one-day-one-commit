#124page 람다식 

def mypower(a):
    data=9*a+2000
    return data


first = mypower(8)
print(first)
print( mypower(8) )
print()
print('람다함수 시작')

last = (lambda b : 9*b+2000) (8)
print(last)
print( (lambda b : 9*b+2000) (8))

