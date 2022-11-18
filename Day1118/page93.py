# numbers = [1,2,3,4,5]
# square = []

# for i in numbers :
#     if i >= 3:
#         square.append(i**2)
#     else :
#         square.append(i+100)

# print(square)
# print()


print('컴프리핸션')
numbers = [1,2,3,4,5]
square = []
square = [i**2 if i>=3 else (i+100) for i in numbers]

# web 문서에서 데이터 입력시 무조건 문자로 인식
# 파이썬에서  변수 = input('가격입력>>') #문자로 인식 2700
# 99페이지
su = 97
pi=3.1415
print('정수 = %d 실수 = %f' %(su, pi))
print('정수 = %d 실수 = %.2f' %(su, pi))
print('정수 = %d 실수 = %7.2f' %(su, pi))
print(round(pi,2))

print()