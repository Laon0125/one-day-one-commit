data = [
    [4,2,3,1],
    [5,6,7,8],
    [9,10,11,12]
    ]
    
print(len(data),'행',len(data[0]))
cnt1 = 0
cnt2 = 0

for a in data :
    data2 = data[cnt1]
    cnt1 += 1
    cnt2 = 0
    for b in data2 :
        
        print(data2[cnt2], end="\t ")
        cnt2 += 1
    print()

#or 
for a in range ( len(data) ) :
    for b in range ( len(data[a])) :
        print (data[a][b], end='\t')
    print()
    
    


