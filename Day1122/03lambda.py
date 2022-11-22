# 124p 람다식 키워드 
def myAdd(x,y) :
    return x+y

print('일반함수 적용')
first = myAdd(8,7)
print(first)
print (myAdd(8,7))
print ()

print('람다함수 적용')
last = (lambda a,b : a+b ) (8,7)
print (last)
print (lambda a,b: a+ b ) (8+7)

