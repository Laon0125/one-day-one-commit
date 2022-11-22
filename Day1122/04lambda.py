# 124p 람다식 키워드 + if 제어문
def myCompare(x,y) :
    if x > y :
        return x
    else :
        return y

print('일반함수 적용')
first = myCompare(8,7)
print(first)
print (myCompare(8,7))
print ()

print('람다함수 적용')
last = (lambda a,b : a if a > b  else b) (8,7)
print (last)
print ((lambda a,b : a if a > b else b) (8,7))



