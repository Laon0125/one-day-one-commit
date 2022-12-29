# 12tuple.py
'''
myList
myTuple
MySet
myDuct for 반복문으로 출력
'''

pos = (
    '양재',
    36.32423,
    127.123123, 
    "시청", 
    37.123145, 
    126.941231
    )
print(pos)
# ('양재', 36.32423, 127.123123, '시청', 37.123145, 126.941231)
for index,b in enumerate(pos) :
    print(index,":", b)
'''
0 : 양재
1 : 36.32423
2 : 127.123123
3 : 시청
4 : 37.123145
5 : 126.941231
'''

print()

for a in range (len(pos)):
    print(pos[a])

'''
양재
36.32423
127.123123
시청
37.123145
126.941231
'''
