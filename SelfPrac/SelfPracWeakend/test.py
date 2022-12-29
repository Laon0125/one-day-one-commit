score_list = [90, 80, 50, 77, 63, 67, 82, 34]
score_dict = {
    '김자바' : [90, 80],
    '이합격' : [50, 77],
    '박이썬' : [63, 67],
    '고길동' : [82, 34],
    '가나다' : [50,77]
            }
for name, score in score_dict.items():
    score_dict.update({name:[score[0] + score[1],(score[0] + score[1])/2]})
rank =[]
for val in score_dict.values() :
    rank.append(val[1])
rank.sort()
rank.reverse()
rank_dict = {}
j=0
for i in rank :
    if i == rank[j-1]:
        pass
    else :
        rank_dict[i] = j
        j += 1
for key, val in score_dict.items():
    if val[1] in rank_dict:
        score_dict.update(
            {key : [val[0] + val[1],(val[0] + val[1])/2, rank_dict[val[1]]+1]}
            )
    else:
        pass
print('이름\t총합\t평균\t순위')
for key,val in score_dict.items():
    print(f'{key}\t{val[0]}\t{val[1]}\t{val[2]}')



