
def main():
    '''
       키보드로 입력된 값이 "yes" or "YES" or "Yes" 이면 "Yes"을 출력하고 아니면 "No"를 출력하는 코드를 작성하시오.

       입력: yes
       출력: Yes

    '''
    s = input("입력:")
    mesg = None
    ####### 구현 시작 ################
    if s == 'yes' or s == "YES" or s == "Yes":
        mesg = 'Yes'
    else : mesg = 'No'

    ########구현 끝 #######################

    print("-------------------------------------------------------------------------------")
    print(mesg)
    print("-------------------------------------------------------------------------------")


# # 메인 함수 호출 ##
if __name__ == "__main__":
    main()