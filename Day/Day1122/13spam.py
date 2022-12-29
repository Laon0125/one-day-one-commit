
u = "<<<  spam<><> aws ham  >>>"
print(u)
print()

#문제 < > <> 특수문자제거  strip(), lstrip(),rstrip() 
#문제 replace함수 spam대신 tomato and egg
#문제 단어word로 쪼개기 split함수 ['tomato', 'and', 'egg', 'and', 'ham']


result = u.strip("<> ")  #strip는 앞뒤 제거할 문자를 지정(문자열을 전처리)
print(result)
result2 = result.replace("<>", "")
print(result2)
result3 = result2.replace("spam", "tomato and egg")
print(result3)
print()
lst = result3.split() 
print( lst )
