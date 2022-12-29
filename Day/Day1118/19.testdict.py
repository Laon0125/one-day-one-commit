# 19tesetdict.py

menu = {} #dict만 사용, 리스트, 튜플 셋 사용금지 
flag = True
input_Num = 0

# flag 가 False 가 될떄 종료
while flag:
    print() # 라인개행
    print("1.등록 2.조회 3.수정 4.삭제 5.검색 9.종료") # 사용자에게 출력
    input_Num=int(input('번호선택 >>>')) # 번호를 입력하게함 입력된 번호를 input_Num에 저장

    # 9.종료 구현
    if input_Num == 9 :
        # 정말 끝내는가?
        really_End = input('정말로 마치시겠습니까? (ㅇㅇ/ㄴㄴ)')
        # 그렇다네요
        if really_End == "ㅇㅇ" :
            flag = False 
            print('저희 프로그램을 이용해 주셔서 감사합니다')

        # 안끝낸데.. 잘못눌럿데
        elif really_End == "ㄴㄴ" :
            flag = True
            print('시작화면으로 돌아갑니다')
            continue
        # ㅇㅇ ㄴㄴ 안누른거 보면 잘못누른듯
        else :
            print('입력값이 올바르지 않습니다, 시작화면으로 돌아갑니다')
            continue
    # 1.등록 구현    
    elif input_Num == 1 : 
        # 등록할 메뉴의 키값을 받는다
        new_Menu = str(input("등록하실 메뉴를 입력하세요 >>"))
        # 등록할 메뉴의 가격을 받는다
        new_Price = int(input('등록하실 메뉴의 가격을 입력하세요 >>>'))
        # 등록한다
        menu[new_Menu] = new_Price

    # 2.조회 구현
    elif input_Num == 2 :
        # 예외처리 등록된 메뉴가 없으면 len(dict)가 0이겟죵
        if len(menu) == 0 : 
            print("등록된 메뉴가 존재하지 않습니다.\n등록 후 이용해주세요")
            continue
        
        # 메뉴보여주기
        else :
            for exist_Menu in menu :
                print(exist_Menu, ':', menu[exist_Menu])
    
    # 3.수정 구현
    elif input_Num == 3 : 
        # 예외처리 2
        if len(menu) == 0 :
            print('수정하실 메뉴가 존재하지 않습니다.')
            continue
        
        # 메뉴가 하나라도 존재한다면 수정가능
        else :
            # 메뉴보여주기
            for exist_Menu in menu :
                print(exist_Menu, ':', menu[exist_Menu])

            edit_Menu = '' # 수정된 키값을 담을 변수
            edit_Menu = str(input('수정하실 메뉴를 입력하세요 >>>')) # 유저 입력으로 수정

            # in 사용해서 edit_Menu가 Menu 안에 존재하는지 확인
            if edit_Menu in menu :
                edit_Price = 0 # 수정할 가격
                orig_Price = menu[edit_Menu] # 초기 설정한 가격
                edit_Price = int(input("수정하실 금액을 입력하세요 >>>")) # 수정금액 입력
                menu[edit_Menu] = edit_Price # 입력된 금액을 대입
                print(orig_Price,' 원 에서 ',edit_Price,
                ' 원 으로 수정되었습니다') 
            # 유저가 입력한 가격이 존재하지 않을떄
            else :
                print('존재하지 않는 메뉴입니다.')
                continue
    
    # 4.삭재 구현
    elif input_Num == 4 : 
        # 예외처리 3
        if len(menu) == 0 :
            print('삭제하실 메뉴가 존재하지 않습니다.')
            continue

        else :
            # 메뉴를 한번 보여준다
            for exist_Menu in menu :
                print(exist_Menu, ':', menu[exist_Menu])
            del_Menu = str(input("삭제하실 메뉴의 이름을 입력하세요>>>")) # 삭제할 메뉴를 유저가 입력
            del menu[del_Menu] #삭 ㅋ 제 
            print(del_Menu, " 메뉴가 삭제되었습니다")
        
    # 5.검색 구현
    elif input_Num == 5 : 
        # 예외처리 4
        if len(menu) == 0 :
            print('등록된 메뉴가 없습니다.')
            continue
        
        #메뉴가 있을떄
        else :
            # 유저가 찾을 메뉴를 저장할 search_Menu 선언 후 입력
            search_Menu = ""
            search_Menu = str(input("찾으시는 메뉴를 입력하세요>>")) 

            # search_Menu 가 menu 안에 있다면
            if search_Menu in menu :
                print(search_Menu,' 의 가격은 ', menu[search_Menu], ' 원 입니다.')
            
            # search_Menu 가 menu 안에 없다면
            else:
                print(search_Menu, "는 존재하지 않는 메뉴입니다")
                continue
        
