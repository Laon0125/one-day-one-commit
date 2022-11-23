#124page 람다식lambda키워드
def myadd(x,y,z):
    gob = x*y*z
    return gob

print('일반함수 적용')
first = myadd(3,2,5)
print(first)
print( myadd(3,2,5) )
print()

print('람다함수 적용')
last = (lambda a,b,c :a*b*c) (3,2,5)
print(last)
print( (lambda a,b,c :a*b*c) (3,2,5))
two = lambda a,b,c :a*b*c
print(two(3,2,5))
