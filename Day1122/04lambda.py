#124page 람다식lambda키워드 + if제어문
def myadd(x,y):
    if x>y:
        return x
    else:
        return y

print('일반함수 적용')
first = myadd(8,47)
print(first)
print( myadd(8,47) )
print()

print('람다함수 적용')
last = (lambda a,b :a if a>b else b) (8,47)
print(last)
print( (lambda a,b :a if a>b else b) (8,47))

