# posasi2000@naver.com

score_Dict = {
    'Lee': [50,77],
    'Park': [63,67],
    'Kim': [90,80],
    'Koh': [82,34],
    'kah': [27,100]
}

#문제, 개인별 총점
'''     총점     평균         총점

Lee     127     63.5        3
Park    130     65          2
Kim     170     85.5        1
Koh     116     58          4
Kah     127     63.5        3

'''

score_List = list()

print()
print('이름\t', '총점\t', '평균\t', '순위')

def find_Sum(dict,k) :
    two_Score = list(dict[k])
    score_Sum = sum(two_Score)
        
    return score_Sum

sorted_sum_list = list()

for i in score_Dict :
    sorted_sum_list.append(find_Sum(score_Dict,i))

sorted_sum_list.sort()
sorted_sum_list.reverse()
    
def rank(number) :

    for n in range (len(sorted_sum_list)) :
        if number == sorted_sum_list[n] :
            return n+1


for j in score_Dict :
    a = find_Sum(score_Dict,j)
    print(j, '\t', a, '\t', a/2, rank(a))

    





