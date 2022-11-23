#124page 람다식lambda키워드 
def myadd(x,y):
    return x+y

print('일반함수 적용')
first = myadd(8,7)
print(first)
print( myadd(8,7) )
print()

print('람다함수 적용')
last = (lambda a,b : a+b) (8,7)
print(last)
print( (lambda a,b : a+b) (8,7))

