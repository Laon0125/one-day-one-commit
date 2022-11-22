def myPower(a) :
    data = 9 * a + 2000
    return data

first = myPower(8)
print (first)
print(myPower(8))
print()
print('람다함수 시작')

last = (lambda b : 9*b+2000) (8)
print(last)
print ( (lambda b : 9*b+2000)(8))