# 05dictfruit.py
# 66p 참고


fruit_Code = {
    '사과' : 101,
    '배' : 102,
    '딸기':103,
    '포도':104,
    '바나나':105
    }

print(fruit_Code)
print(fruit_Code.keys())
print(fruit_Code.values())
print()
print(fruit_Code.items())

# 67p 참고
fruit_Code2 = {'오랜지':106, '수박':107}
fruit_Code.update(fruit_Code2)
print()

fruit_Code.clear()
print(fruit_Code)
