def main():
    '''
    입력으로 제공되는 점수 리스트를 이용하여, 최소값과 최대값을 제외한 점수의 합계를 계산하는 프로그램을 작성하시오.
 (단, 중복되는 값은 없음)
입력 예시1) [35, 78, 88, 99, 72], 최대값과 최소값을 제외한 점수) 78, 88, 72 출력 예시1) 238
입력 예시2) [55, 90, 80, 45, 70], 최대값과 최소값을 제외한 점수) 55, 80, 70 출력 예시2) 205

    '''

    # 입력 : 점수 리스트
    score = [55, 90, 80, 45, 70]
    #score = [35, 78, 88, 99, 72]

    score_sum = None
    ####### 구현 시작 ################
    sorted_score_list = sorted(score)
    print(sorted_score_list)
    score_sum = sum(sorted_score_list[1:-1])
    print(score_sum)
    ########구현 끝 #######################

    # 계산된 합을 출력
    print("-------------------------------------------------------------------------------")
    print("최솟값과 최댓값을 뺀 값의 합 : ", score_sum)
    print("-------------------------------------------------------------------------------")

# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()
