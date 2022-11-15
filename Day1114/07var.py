a,b = 9,4
#합계 빼기 곱 몫 나머지
total, sub, mul, mok, nmg = 0, 0, 0, 0, 0
a, b = 9,4
total = a + b
sub = a - b
mul = a * b
mok = a / b
nmg = a % b

print(a, '+', b, '=', total)
print(a, '-', b, '=', sub)
print(a, '*', b, '=', mul)
print(a, '/', b, '=', mok)
print(a, '%', b, '=', nmg)

print(f'{a}+{b}={total}')
print(f'{a}-{b}={sub}')
print(f'{a}*{b}={mul}')
print(f'{a}/{b}={mok}')
print(f'{a}%{b}={nmg}')