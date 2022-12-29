test_List = list(range(1,1000000))
test_List.sort()
sorted_Test_List = test_List

# 속도비교를 위한 순차적으로 찾는 함수
def search_From_Front(list_List) :
    input_Num = int(input('찾으시는 숫자를 입력하세요>>>'))
    counter = 0
    for i in list_List :
        counter += 1
        if i == input_Num :
            print(i)
            print(counter, ' 회 안에 찾았습니다')
            
search_From_Front(sorted_Test_List)

def binery_Search (list_List) :
    length_of_List = len(list_List) - 1
    counter = 0
    small_Index = 0
    input_Num = int(input('찾으시는 숫자를 입력하세요>>>'))
    big_Index = length_of_List
    while small_Index <= big_Index:
        counter+=1
        middle_Index = int((big_Index+small_Index)/2)
        if list_List[middle_Index] == input_Num :
            print(list_List[middle_Index])
            
            print(counter, ' 회 안에 찾았습니다')
            break
        if list_List[middle_Index] < input_Num :
            small_Index = middle_Index + 1
            continue
        if list_List[middle_Index] > input_Num :
            big_Index = middle_Index-1 
            continue
    
binery_Search(sorted_Test_List)
     
        
    




    
    