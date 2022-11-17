data =[
 [54,53,52,51] ,    #0행 4열
 [8,7,6,4,3,2,1] ,        #1행 7열
 [9,10,11]       #2행 3열
]
cnt1 = 0
for a in data :
    data2 = data[cnt1]
    cnt1 += 1
    cnt2 = 0
    for b in data2 :
        
        print(data2[cnt2], end="\t ")
        cnt2 += 1
    print()