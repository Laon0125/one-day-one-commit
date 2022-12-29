def solution(common):
    answer = 0
    temp_list = list(common)
    difference = 0
    if temp_list[1] - temp_list[0] == temp_list[2] - temp_list[1] :
        difference = temp_list[1] - temp_list[0]
        answer = temp_list[len(temp_list) - 1] + difference

    else :
        difference = temp_list[1] / temp_list[0]
        answer = int(temp_list[len(temp_list) - 1] * difference)
    
    return answer

print(solution([1, 2, 4, 8]))