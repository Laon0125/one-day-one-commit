# 숫자를 왼쪽정렬
for x in range (1,6) :
    print(x, '*',x, '=', x*x)

# d오른쪽으로 정렬
for x in range (1,6) :
    print(x, '*',x, '=', str(x*x).rjust(5))

for x in range (1,6) :
    print(x, '*',x, '=', str(x*x).zfill(5))

print('=' * 100)
print()


