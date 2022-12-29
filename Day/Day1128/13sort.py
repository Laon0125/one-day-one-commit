a = [4,7,5,1,2,9,3,6,8]
# 소트 = 선택, 버블, 삽입, 이진, 힙
print()

'''
1   7   5   4   2
1   2   7   5   4
1   2   4   7   5
1   2   4   5   7
'''
# 선택 selection sort
print()
i = 0
j = 1
for i in range (len(a)-1) :
    for j in range (i + 1, len(a)) :
        if a[i] > a[j] :
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            
print (a)
