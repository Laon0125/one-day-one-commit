def main():
    '''
    제공되는 성적목록의 순서대로 각 성적의 학점을 계산하는 프로그램을 작성하시오.
(조건, 각 성적은 0~100 이며, 90~100 A, 80~89 B, 70~79 C, 60~69 D, 0~59 F 이다.)
입력1) 89, 75, 56, 39, 95, 100, 88, 65
출력1) ['B', 'C', 'F', 'F', 'A', 'A', 'B', 'D']
입력2) 35, 85, 66, 78, 99, 40, 100, 89
출력2) ['F', 'B', 'D', 'C', 'A', 'F', 'A', 'B']
    '''

    # 입력 : 성적 목록
    scores = [89, 75, 56, 39, 95, 100, 88, 65]
    scores = [35, 85, 66, 78, 99, 40, 100, 89]

    temp_list = []
    ####### 구현 시작 ################

    ########구현 끝 #######################
    
    print("-------------------------------------------------------------------------------")
    print("계산된 학점 목록: ", temp_list)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
