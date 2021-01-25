'''
회원관리 프로그램을 작성
    - 회원정보 : 회원번호, 이름, 전화번호
    - 회원번호를 사용해서 이름과 전화번호를 관리

1. 회원추가     2. 회원검색     3. 회원삭제     4. 회원목록      0. 종료
'''



change = True

memberlst = dict()

while change:
    print("1. 회원추가     2. 회원검색     3. 회원삭제     4. 회원목록      0. 종료")    
    select = int(input("원하시는 서비스를 선택해 주세요 > "))
    
    if select == 1: # 회원추가
        memberNum = input("회원번호 입력 > ")
        memberName = input("회원이름 입력 > ")
        memberPhone = input("회원전화번호 입력 > ")
        memberInfo = (memberNum, memberName, memberPhone)
        memberlst.append(memberInfo)
        print(memberlst)

    elif select == 2: # 회원검색
        memberFind = input("찾으시는 회원번호를 입력해 주세요 > ")
        if memberFind == memberlst.index(memberFind):
            print(memberlst.index(memberFind))
        else:
            print("존재하지 않는 회원번호입니다.")

    elif select == 3: #회원삭제        
        memberdelete = input("삭제하려는 회원번호를 입력해 주세요 > ")
        if memberdelete == memberNum:
            memberlst.pop(memberNum)
            print("{}번의 회원을 삭제하였습니다.".format(memberdelete))
        else:
            print("존재하지 않는 회원번호입니다.")

    elif select == 4: # 회원목록        
        print(memberlst)

    elif select == 0: # 종료
        change = False

    else:
        print("정확하게 입력해주세요.")
