def solution(num, total):
    answer = []
    middle = total / num
    
    if num % 2 == 1 :
        small = int(middle - (num/2) + 0.5) 
    else  :
        small = int(middle + 0.5 - (num/2))
    
    counter = 0
    
    for i in range(0,num):
        answer.append(small)
        small += 1
        
        
    return answer

print(solution(3,12))