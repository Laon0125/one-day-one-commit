# 124p 람다식 키워드 + if 제어문
def myMult(x,y,z) :
    return x*y*z

print('일반함수 적용')
first = myMult(8,7,5)
print(first)
print (myMult(8,7,5))
print ()

print('람다함수 적용')
last = (lambda a,b,c : a*b*c) (8,7,5)
print (last)
print ((lambda a,b,c : a*b*c) (8,7,5))
two = ((lambda a,b,c, : a*b*c) (3,2,5))
print (two)
