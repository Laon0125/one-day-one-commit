# bubble_Sort.py
# bubble sort 를 구현

a = [6,2,8,4,3]

'''
6   2   8   4   3  
2   6   8   4   3
2   6   4   8   3
2   6   4   3   8
2   4   6   3   
2   4   3   6
2   3   4
2   3
2
'''

def bubble_Sort(listA):
    
    for i in range (len(listA)-1, 0, -1):
        for j in range (0,i,1):
            if listA[j] >listA[j+1] :
                tmp = listA[j]
                listA[j] = listA[j+1]
                listA[j+1] = tmp
    return listA 

print(bubble_Sort(a))

