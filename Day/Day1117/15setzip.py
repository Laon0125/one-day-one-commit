#15setzip.py

wish = {
    'apple',
    'blue',
    'cherry'
}
num = [80,20,30]

for data in zip(wish,num) :
    print(data)

#sorting 안돼있는 리스트에 소팅하고 인덱스 붙이는 용도?
# ex) 정렬안된 점수리스트를 정렬후 순위매기기?


'''
wish = {
    'apple',
    'blue',
    'cherry'
}

print(wish)
wish.add('양제역')
print(wish)
wish.discard('늦가을')
print(wish)
'''