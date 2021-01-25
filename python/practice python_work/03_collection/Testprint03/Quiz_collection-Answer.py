

# Quiz_collection.py

'''
회원관리 프로그램을 작성하세요
- 회원정보 : 회원번호, 이름, 전화번호
- 회원번호를 사용해서 이름과 전화번로를 관리합니다

1.회원추가  2.회원검색  3.회원삭제  4.회원목록  0.종료
'''
member = dict()

memberRun = True
while memberRun:
    print("1.회원추가  2.회원검색  3.회원삭제  4.회원목록  0.종료")
    select = int(input("선택 >> "))

    if select == 1: # 추가
        print("---  회 원 추 가  ---")
        id = input("회원번호 입력 > ")
        name = input("이름 입력 > ")
        phone = input("전화번호 입력 > ")
        data = [name, phone]
        info = data.copy()
        member.setdefault(id, info)
        data.clear()

    elif select == 2: # 검색
        print("---  회 원 검 색  ---")
        search = input("회원번호 입력 > ")
        if member.get(search) == None:
            print("없는 회원번호 입니다~")
        else:
            for id, info in member.items():
                if id == search:
                    print("{} : {} - {}".format(id, info[0], info[1]))

    elif select == 3: # 삭제
        print("---  회 원 삭 제  ---")
        remove = input("회원번호 입력 > ")
        if member.get(remove) == None:
            print("없는 회원번호 입니다~")
        else:
            print(member.pop(remove), " 삭제")

    elif select == 4:
        print("---  회 원 목 록  ---")
        for id, info in member.items():
            print("{} : {} - {}".format(id, info[0], info[1]))
        print()

    elif select == 0:
        memberRun = False

    else:
        print("선택 오류~")

else:
    print("- Program end -")
    





















