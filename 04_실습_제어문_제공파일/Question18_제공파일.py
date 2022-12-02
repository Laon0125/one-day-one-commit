
def main():
    '''
   15.	List comprehension을 사용하여 입력된 리스트중에서 5와 7로 나누어 지는 값을 제거하고 출력하는 코드를 작성하시오.


입력: [12,24,35,70,88,120,155]
출력: [12, 24, 88]


    '''
    input_data = [12,24,35,70,88,120,155]
    output_data = []

    ####### 구현 시작 ################
    output_data = ( [x for x in input_data if x % 7 != 0 and x % 5 !=0 ])
    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(output_data)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
