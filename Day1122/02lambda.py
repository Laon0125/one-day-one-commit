#124page 람다식 

def mypower(a):
    data=4*a+2000
    return data

print('일반함수 적용')
first = mypower(8)
print(first)
print( mypower(8) )
print()

print('람다함수 적용')

last = (lambda b : 4*b+2000) (8)
print(last)
print( (lambda b : 4*b+2000) (8))

